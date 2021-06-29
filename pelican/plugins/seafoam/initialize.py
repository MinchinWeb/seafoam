import logging

from .constants import LOG_PREFIX, __version__

logger = logging.getLogger(__name__)


def seafoam_version(pelican):
    """
    Insert seafoam version into Pelican context.
    """

    if "SEAFOAM_VERSION" not in pelican.settings.keys():
        pelican.settings["SEAFOAM_VERSION"] = __version__
        logger.debug(
            "%s Adding Seafoam version (%s) to context." % (LOG_PREFIX, __version__)
        )
    else:
        logger.debug(
            "%s SEAFOAM_VERSION already defined (%s)." % (LOG_PREFIX, pelican.settings["SEAFOAM_VERSION"])
        )
