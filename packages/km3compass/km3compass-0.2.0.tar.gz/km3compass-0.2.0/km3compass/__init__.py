from pkg_resources import get_distribution, DistributionNotFound

version = get_distribution(__name__).version

from .tools import *
from .readerCSK import readerCSK
from .readerOnline import readerOnline
from .calibration import (
    calib_DB,
    calib_self_sphere,
    calibration_DB_agent,
    detector_calibration,
)
from .acceptance_tests import acceptance_test
