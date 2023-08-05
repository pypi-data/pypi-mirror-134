from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

# IMPORT LOCAL
from mosaici.exceptions import *

from mosaici.base_mosaic import BaseMosaicFile, BaseMosaicFileTemplate, BaseMosaicMultiTemplate, BaseMosaicMultiFile
from mosaici.template import Template, FileTemplate
from mosaici.store import StoreFileIndexes, StoreObjectIndexes
from mosaici.indexpack import FilePathIndexes

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

"""
Mosaic Object - All Mosaic Module Instance Of BaseMosaic
"""

# STANDARD MOSAIC FILE
class MosaicFile(BaseMosaicFile):
    """
    MosaicFile - Instance of BaseMosaicFile
    This Module Customized For Working Easy and Better With File
    """
    TEMPLATE: Template = Template
    ACTIVE_MAKER: bool = None
    FILE_TEMPLATE: FileTemplate = FileTemplate
    STORE_INDEXES: StoreFileIndexes = StoreFileIndexes
    FILE_INDEXES: FilePathIndexes = FilePathIndexes


# STANDARD MOSAIC
class MosaicObject(BaseMosaicFileTemplate):
    """
    Mosaic - Instance of BaseMosaicFileTemplate
    """
    TEMPLATE: Template = Template
    ACTIVE_MAKER: bool = True
    FILE_TEMPLATE: FileTemplate = FileTemplate
    STORE_INDEXES: StoreObjectIndexes = StoreObjectIndexes


# STANDARD MOSAIC MULTI TEMPLATE
class MosaicMulti(BaseMosaicMultiTemplate):
    """
    MosaicMulti- Instance of BaseMosaicMultiTemplate
    This Module Customized For Working Easy and Better With File
    """
    TEMPLATE: Template = Template
    ACTIVE_MAKER: bool = False
    FILE_TEMPLATE: FileTemplate = FileTemplate
    STORE_INDEXES: StoreObjectIndexes = StoreObjectIndexes


# MOSAIC MULTI FILE
class MosaicMultiFile(BaseMosaicMultiFile):
    """
    MosaicMultiFile- Instance of BaseMosaicMultiTemplate
    This Module Customized For Working Easy and Better With File
    """
    TEMPLATE: Template = Template
    FILE_TEMPLATE: FileTemplate = FileTemplate
    STORE_INDEXES: StoreFileIndexes = StoreFileIndexes
    FILE_INDEXES: FilePathIndexes = FilePathIndexes



__dir__ = (
    'MosaicFile',
    'MosaicObject',
    'MosaicMulti',
    'MosaicMultiFile',
    )
