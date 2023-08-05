#!/usr/bin/env python3
import km3db
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from .tools import cart2AHRS


class calibration_DB_agent:
    """
    Handle DB request to speed up things
    """

    def __init__(self):
        print("Starting a new calibration DB agent ...")
        start = np.datetime64("now")
        self.sds = km3db.tools.StreamDS(container="pd")
        self.CLB_UPIs = self.sds.clbid()
        self.calibs = self.sds.ahrscalib().sort_values(["REVTIMEORDER"])
        self.load_CLB2CompassMap()
        print("Done in {}".format(str(np.datetime64("now") - start)))

    def load_CLB2CompassMap(self):
        """Load the table to create CLB to compass map"""
        df = self.sds.integration(CONTENT_UPI="*AHRS*")
        df = pd.concat((df, self.sds.integration(CONTENT_UPI="*LSM303*")))
        self.compass = df[
            (df["CONTENT_UPI"].str.contains("AHRS"))
            | (df["CONTENT_UPI"].str.contains("LSM303"))
        ]

    def get_CLB_UPI(self, mac_address):
        """
        Return CLB UPI from mac address

        Parameters:
        -----------
        mac_address: str
          DOM mac address, lower case expected.
        """
        df = self.CLB_UPIs[self.CLB_UPIs["MACADDR"].str.lower() == mac_address]
        return df.iloc[0]["CLBUPI"]

    def get_compass_UPI(self, CLB_UPI):
        """
        Return compass UPI from CLB UPI

        Compass calibration is selected by taking the smaller
        REVTIMEORDER for a given compass serial number. More details
        in this git issue:
        https://git.km3net.de/common/km3web/-/issues/46#note_21808

        Parameters:
        -----------
        CLB UPI: str
          CLB UPI in string format
        """
        df = self.compass[self.compass["CONTAINER_UPI"] == CLB_UPI]
        return df.iloc[0]["CONTENT_UPI"]

    def get_calibration(self, compass_SN):
        """
        Return calibration constants from compass serial number

        Parameters:
        -----------
        compass_SN: int
          Compass serial number
        """
        df = self.calibs[self.calibs["SERIALNUMBER"] == compass_SN]
        return df.iloc[0]  # Take the smaller REVTIMEORDER


class calib_DB:
    """
    Module for applying calibration from DB

    Parameters:
    -----------
    reader: km3compass reader object
      Reader object, either CSK or -something else-
    moduleID: int
      DOM module ID inside the file.
    calibrate: bool, default = True
      Apply or not the calibration. Can be turned off to modify calibration.
    db_agent: calibration_DB_agent object
      Provide external calibration_DB_agent object, avoiding additional query to DB
    """

    def __init__(self, reader, moduleID, calibrate=True, db_agent=None, verbosity=True):
        self.moduleID = moduleID
        self.db_agent = db_agent
        self.verbosity = verbosity
        self.df = reader.df
        self.df = self.df[self.df["DOMID"] == self.moduleID]

        self.mac_address = "0800" + hex(self.moduleID)[2:]
        # Probably a better way to do this, but anyway ...
        self.mac_address = (
            self.mac_address[:2]
            + ":"
            + self.mac_address[2:4]
            + ":"
            + self.mac_address[4:6]
            + ":"
            + self.mac_address[6:8]
            + ":"
            + self.mac_address[8:10]
            + ":"
            + self.mac_address[10:]
        )
        if self.verbosity:
            print("DOM mac address : {}".format(self.mac_address))

        if calibrate:
            try:
                self.calibrate()
            except Exception as E:
                if verbosity:
                    print(E)
                self.df = None

    def calibrate(self):
        """Apply calibration chain"""
        self.load_calibration()
        self.apply_calibration()

    def load_calibration(self):
        """
        Load calibration from km3net webdb

        This is done in steps :
        #. Mac address conversion to CLB UPI
        #. CLB UPI to compass UPI
        #. Get calibration from ahrscalib streamDS
        """

        # Initialize calibration row
        self.row_calib = None
        self.compassVariant = ""

        # Check for external DB agent
        if self.db_agent is None:
            self.db_agent = calibration_DB_agent()

        # Get CLB UPI
        self.CLB_UPI = self.db_agent.get_CLB_UPI(self.mac_address)

        # Get Compass UPI
        self.compass_UPI = None

        try:
            self.compass_UPI = self.db_agent.get_compass_UPI(self.CLB_UPI)
        except:
            raise KeyError("CLB not found : {}".format(self.CLB_UPI))

        # Extract compass serial number
        self.compassSN = int(self.compass_UPI.split(".")[-1])
        self.compassVariant = self.compass_UPI.split("/")[1]

        # Check if floor ID == 0
        # If yes, it's a base module : no calibration
        if "FLOORID" in self.df.columns:
            if self.df.FLOORID.iloc[0] == 0:
                raise KeyError(
                    "No calibration expected, {} is a base module.".format(
                        self.moduleID
                    )
                )

        # Get the calib from ahrscalib streamDS
        try:
            self.row_calib = self.db_agent.get_calibration(self.compassSN)
        except:
            raise KeyError("No calibration found : {}".format(self.compass_UPI))

        self.row_calib["DOMID"] = self.moduleID

        # Format in a easily accesisble
        magMinMax = []
        labelMagRot = []
        labelAccRot = []
        accOffset = []

        for i in ["X", "Y", "Z"]:
            magMinMax.append(
                self.row_calib[["MAG_{}MIN".format(i), "MAG_{}MAX".format(i)]].values
            )
            accOffset.append(self.row_calib["ACC_OFFSET_{}".format(i)])
            for j in ["X", "Y", "Z"]:
                labelMagRot.append("MAG_ROT_{}{}".format(i, j))
                labelAccRot.append("ACC_ROT_{}{}".format(i, j))

        magMinMax = np.array(magMinMax, dtype=float)
        magCenter = -np.mean(magMinMax, axis=1)
        accOffset = -np.array(accOffset, dtype=float)
        magRot = np.reshape(self.row_calib[labelMagRot].values, (3, 3)).astype(float)
        accRot = np.reshape(self.row_calib[labelAccRot].values, (3, 3)).astype(float)

        self.calib = {
            "magMinMax": magMinMax,
            "magOffset": magCenter,
            "magRot": magRot,
            "accRot": accRot,
            "accOffset": accOffset,
        }

    def apply_calibration(self):
        """
        Apply calibration on df.

        Equivalent to the implementation in JPP ``JDETECTOR::JCompass::JCompass``
        https://common.pages.km3net.de/jpp/classJDETECTOR_1_1JCompass.html
        """
        a = self.df[["AHRS_A0", "AHRS_A1", "AHRS_A2"]].values
        a_calibrated = (
            self.calib["accRot"].dot((a + self.calib["accOffset"][np.newaxis, :]).T).T
        )

        h = self.df[["AHRS_H0", "AHRS_H1", "AHRS_H2"]].values
        h_calibrated = (
            self.calib["magRot"].dot((h + self.calib["magOffset"][np.newaxis, :]).T).T
        )

        for i in range(3):
            self.df["AHRS_A{}".format(i)] = a_calibrated[:, i]
            self.df["AHRS_H{}".format(i)] = h_calibrated[:, i]

    def print_calibration(self):
        """Print a summary of the calibration file"""
        print("CLB {}, compass calibration".format(self.CLB_UPI))
        print(" - mac address : {}".format(self.mac_address))
        print(" - compass UPI : {}".format(self.compass_UPI))
        print()
        print(
            " - mag offset  : {:.3f}, {:.3f}, {:.3f}".format(*self.calib["magOffset"])
        )
        print(
            " - mag rotmat  : {:.3f}, {:.3f}, {:.3f}".format(*self.calib["magRot"][0])
        )
        print(
            "                 {:.3f}, {:.3f}, {:.3f}".format(*self.calib["magRot"][1])
        )
        print(
            "                 {:.3f}, {:.3f}, {:.3f}".format(*self.calib["magRot"][2])
        )
        print()
        print(
            " - acc offset  : {:.3f}, {:.3f}, {:.3f}".format(*self.calib["accOffset"])
        )
        print(
            " - acc rotmat  : {:.3f}, {:.3f}, {:.3f}".format(*self.calib["accRot"][0])
        )
        print(
            "                 {:.3f}, {:.3f}, {:.3f}".format(*self.calib["accRot"][1])
        )
        print(
            "                 {:.3f}, {:.3f}, {:.3f}".format(*self.calib["accRot"][2])
        )
        print()

    def get_summary_df(self):
        """Return a calibration summary dataframe"""
        df = pd.DataFrame(
            {
                "DOMID": [self.moduleID],
                "Variant": [self.compassVariant],
                "CLB UPI": [self.CLB_UPI],
                "Compass UPI": [self.compass_UPI],
                "status": [self.row_calib is not None],
            }
        ).set_index("DOMID")

        calib = self.row_calib
        if calib is not None:
            calib = self.row_calib.to_frame().T.set_index("DOMID")

        return pd.concat((df, calib), axis=1)


class calib_self_sphere:
    """
    Module to try calibrate from data itself

    Parameters:
    -----------
    reader: km3compass reader object
      Reader object, either CSK or -something else-
    moduleID: int
      DOM module ID inside the file.
    calibrate: bool, default = True
      Apply or not the calibration. Can be turned off to modify calibration.
    """

    def __init__(self, reader, moduleID):
        self.moduleID = moduleID
        self.reader = reader
        self.df = reader.df
        self.df = self.df[self.df["DOMID"] == self.moduleID]

        self.fit_result = self.sphere_fit(
            self.df["AHRS_H0"].values,
            self.df["AHRS_H1"].values,
            self.df["AHRS_H2"].values,
        )

        self.fit_result = np.array(self.fit_result)

        self.center = self.fit_result[1:]
        self.radius = self.fit_result[0]
        self.apply_calibration()

    def sphere_fit(self, spX, spY, spZ):
        """
        Function to fit a sphere to a 3D set of points

        Full credit to Charles Jekel (https://jekel.me/2015/Least-Squares-Sphere-Fit/)

        Parameters:
        -----------
        spX : numpy array
          X coordinates
        spY : numpy array
          Y coordinates
        spZ : numpy array
          Z coordinates


        Return:
        -------
        Radius, Cx, Cy, Cz
          Radius and x,y,z coordinate of the sphere center
        """
        #   Assemble the A matrix
        spX = np.array(spX)
        spY = np.array(spY)
        spZ = np.array(spZ)
        A = np.zeros((len(spX), 4))
        A[:, 0] = spX * 2
        A[:, 1] = spY * 2
        A[:, 2] = spZ * 2
        A[:, 3] = 1

        #   Assemble the f matrix
        f = np.zeros((len(spX), 1))
        f[:, 0] = (spX * spX) + (spY * spY) + (spZ * spZ)
        C, residules, rank, singval = np.linalg.lstsq(A, f, rcond=None)

        #   solve for the radius
        t = (C[0] * C[0]) + (C[1] * C[1]) + (C[2] * C[2]) + C[3]
        radius = np.sqrt(t)

        return radius, C[0], C[1], C[2]

    def apply_calibration(self):
        """Apply calibration determined with sphere fit"""

        for i, axe in enumerate(["AHRS_H0", "AHRS_H1", "AHRS_H2"]):
            self.df[axe] -= self.center[i]

    def plot_results(self):
        """Plot summary of the fit process"""

        fig = plt.figure(figsize=(12, 6))

        spec = mpl.gridspec.GridSpec(2, 4, fig)

        axe3D = fig.add_subplot(spec[:, :2], projection="3d")
        axeR = fig.add_subplot(spec[0, 3])

        u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
        x = self.radius * np.cos(u) * np.sin(v) + self.center[0]
        y = self.radius * np.sin(u) * np.sin(v) + self.center[1]
        z = self.radius * np.cos(v) + self.center[2]
        axe3D.plot_wireframe(x, y, z, color="C0", linewidth=1)
        axe3D.set_aspect("auto")
        axe3D.set_xlabel("X [G]")
        axe3D.set_ylabel("Y [G]")
        axe3D.set_zlabel("Z [G]")

        df_raw = self.reader.df
        axe3D.scatter(
            df_raw["AHRS_H0"],
            df_raw["AHRS_H1"],
            df_raw["AHRS_H2"],
            color="C3",
            marker=".",
        )

        r = np.sqrt(
            self.df["AHRS_H0"] ** 2 + self.df["AHRS_H1"] ** 2 + self.df["AHRS_H2"] ** 2
        )
        residuals = (r - self.radius) / self.radius * 100.0
        bins = np.linspace(np.min(residuals) * 1.5, np.max(residuals) * 1.5, 21)
        axeR.hist(residuals, bins=bins, histtype="stepfilled", alpha=0.6)
        axeR.set_xlabel("Radius residuals [%]")

        plt.tight_layout()


class detector_calibration:
    """
    Module to calibrate a sea dataset

    This module will iterate over the present module and apply
    calibration. It also produces summary information and provides
    filtering methods.

    Parameters:
    -----------
    reader: km3compass reader object
      Reader object, either CSK or -something else-
    moduleID: int
      DOM module ID inside the file.
    calibrate: bool, default = True
      Apply or not the calibration. Can be turned off to modify calibration.
    """

    def __init__(self, reader, detoid, db_agent=None, calib_module=calib_DB):
        self.reader = reader
        self.detoid = detoid
        self.db_agent = db_agent
        self.calib_module = calib_module

        if self.db_agent is None:
            self.db_agent = calibration_DB_agent()

    def apply_calibration(self):
        """Apply calibration to the provided reader"""

        def get_mod_information(df, modID):
            df = df[df["DOMID"] == modID]
            return df.iloc[[0]][["DOMID", "FLOORID", "DUID"]].set_index("DOMID")

        self.df = None
        self.summary = None
        self.calib_dict = {}

        # Loop over modules
        for modID in np.unique(self.reader.df["DOMID"]):

            calib = calib_DB(
                self.reader, modID, db_agent=self.db_agent, verbosity=False
            )
            self.calib_dict[modID] = calib
            # Create a summary row with calibration information
            summary_row = calib.get_summary_df()
            summary_row = pd.concat(
                (summary_row, get_mod_information(self.reader.df, modID)), axis=1
            )
            # Store summary row
            self.summary = pd.concat((self.summary, summary_row))

            # Calibration not done, pass to next DOM
            if calib.df is None:
                continue
            # Calibration done, store calibrated data in self.df
            self.df = pd.concat((self.df, calib.df), axis=0)

    def print_calibration_summary(self):
        """Print a summary of calibration"""
        n_DOM = len(np.unique(self.reader.df[self.reader.df["FLOORID"] > 0]["DOMID"]))
        n_BM = len(np.unique(self.reader.df[self.reader.df["FLOORID"] == 0]["DOMID"]))

        n_DOM_ok = len(np.unique(self.summary[self.summary["status"]].index))

        print("DOM/BM before calibration: {}/{}".format(n_DOM, n_BM))
        print("DOM after calibration: {}".format(n_DOM_ok))
        print("Details about calibration:")

        self.df_overview = self.summary
        self.df_overview.replace({"0.0": "0"}, inplace=True)
        self.df_overview["n compass"] = np.ones(self.summary.shape[0], dtype=int)
        self.df_overview = self.df_overview.groupby(
            ["DUID", "TESTNAME", "Variant", "FIRMWARE_VERSION"]
        ).sum()["n compass"]
        print(self.df_overview)

        self.df_overview = self.summary
        self.df_overview.replace({"0.0": "0"}, inplace=True)
        self.df_overview["n compass"] = np.ones(self.summary.shape[0], dtype=int)
        self.df_overview = self.df_overview.groupby(
            ["TESTNAME", "Variant", "FIRMWARE_VERSION"]
        ).sum()["n compass"]
        print(self.df_overview)

    def plot_calibration_summary(self):
        """Plot a summary of calibration version per DOM"""

        DUID_map = {}
        for i, duid in enumerate(np.unique(self.summary["DUID"].values)):
            DUID_map[duid] = i

        fig, axe = plt.subplots()
        axe.set_aspect("equal")
        axe.set_xlim((-1, 19))
        print(len(DUID_map))
        axe.set_ylim((-1, len(DUID_map)))

        nodata_kwargs = {
            "hatch": "",
            "edgecolor": [0.4] * 3,
            "facecolor": [0, 0, 0, 0],
            "zorder": 0,
        }
        nocal_kwargs = {
            "hatch": "//",
            "edgecolor": [0.4] * 3,
            "facecolor": [0, 0, 0, 0],
            "zorder": 1,
        }

        def plot_category(coords, axe, kwargs, label=""):
            first = True
            for coord in coords:
                coord = coord.astype(float) - 0.5
                patch = mpl.patches.Rectangle(coord, 1, 1, **kwargs)
                if first:
                    patch = mpl.patches.Rectangle(coord, 1, 1, label=label, **kwargs)
                    first = False
                axe.add_patch(patch)

        df = self.summary[self.summary["status"] == False].copy()

        df["DUID"] = df["DUID"].replace(DUID_map)

        full_array = np.meshgrid(np.arange(19), np.arange(len(DUID_map)))
        full_array = np.reshape(full_array, (2, len(DUID_map) * 19))
        full_array = np.swapaxes(full_array, 0, 1)

        plot_category(
            full_array,
            axe,
            nodata_kwargs,
            label="No data",
        )
        plot_category(
            df[["FLOORID", "DUID"]].values,
            axe,
            nocal_kwargs,
            label="No calibration",
        )

        for it, ind in enumerate(self.df_overview.index):
            label = "{}, calib V{}, fw {}".format(ind[1], ind[0][-1], ind[2])
            kwargs = {"edgecolor": [0.4] * 3, "facecolor": "C" + str(it), "zorder": 1}

            df = self.summary[
                (self.summary["TESTNAME"] == ind[0])
                & (self.summary["Variant"] == ind[1])
                & ((self.summary["FIRMWARE_VERSION"] == ind[2]))
            ].copy()

            df["DUID"] = df["DUID"].replace(DUID_map)
            plot_category(df[["FLOORID", "DUID"]].values, axe, kwargs, label=label)

        axe.set_yticks(list(DUID_map.values()))
        axe.set_yticklabels(list(DUID_map.keys()))
        axe.set_xticks(np.linspace(0, 18, 10, dtype=int))
        axe.set_xlabel("Floor ID")
        axe.set_ylabel("DU ID")

        axe.legend(
            bbox_to_anchor=(0, 1.02, 1, 0.2),
            loc="lower left",
            mode="expand",
            borderaxespad=0,
            ncol=2,
        )

        plt.tight_layout()

        return fig
