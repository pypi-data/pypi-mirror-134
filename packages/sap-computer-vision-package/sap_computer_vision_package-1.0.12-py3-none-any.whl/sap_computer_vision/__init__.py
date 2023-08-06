"""Detectron2 extension. This package extends detectron2 to support image classification and
feature extraction/image retrieval models."""
import pathlib

SAP_COMPUTER_VISION_DIR = pathlib.Path(__file__).parent
DISCLAIMER = SAP_COMPUTER_VISION_DIR / 'DISCLAIMER'
LICENSE = SAP_COMPUTER_VISION_DIR / 'LICENSE'

from .config import get_cfg, get_config_file, setup_loggers
from .engine import *
from .modelling import *

#import sap_computer_vision.examples as _
#import sap_computer_vision.pipelines as _

__all__ = ["config", "get_cfg", "get_config_file", "setup_loggers", "DISCLAIMER", "LICENSE", "SAP_COMPUTER_VISION_DIR"]
