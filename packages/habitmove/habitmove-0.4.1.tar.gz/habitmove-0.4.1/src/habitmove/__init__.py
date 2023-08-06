# init.py
import sys

try:
    from importlib.metadata import version as metadata_version
except ImportError:
    from importlib_metadata import version as metadata_version

__version__ = str(metadata_version(__name__))
