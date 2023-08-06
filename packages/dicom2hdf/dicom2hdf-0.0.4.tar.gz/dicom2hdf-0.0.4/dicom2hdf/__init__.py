import logging

from .data_generators.patient_data_generator import PatientDataGenerator
from .datasets.hdf5_dataset import PatientDataset
from .logging_tools import logs_file_setup

logs_file_setup(__file__, logging.INFO)

__author__ = "Maxence Larose"
__version__ = "0.1.1"
__copyright__ = "Copyright 2022, Maxence Larose"
__credits__ = ["Maxence Larose"]
__license__ = "GPL"
__maintainer__ = "Maxence Larose"
__email__ = "maxencelarose@hotmail.com"
__status__ = "Production"
