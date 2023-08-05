from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# FILE ERROR
class FileIsNotWritableError(IOError):
    pass


# INDEXES ERROR
class IndexesIsNotDefinedError(ValueError):
    pass


# FILE INDEXES ERROR
class AccessDeniedFileIsClosed(IOError):
    pass


# MODE NOT EXISTS -> `ModeName`
class ModeNotExistsError(NameError):
    pass


# ACTION NOT EXISTS -> `ModeName`
class ActionNotExistsError(NameError):
    pass


# FILE ERROR
class FileIsNotReadableError(IOError):
    pass


# TEMPLATE NOT DEFINED - MOSAIC MULTI TEMPLATE
class TemplateNotDefinedError(KeyError):
    pass


# THERE IS NOT ACTIVE TEMPLATE - MOSAIC MULTI TEMPLATE
class ThereIsNotActiveTemplate(ValueError):
    pass
