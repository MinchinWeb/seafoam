import logging

from .constants import LOG_PREFIX, __version__

logger = logging.getLogger(__name__)


def seafoam_version(pelican):
    """
    Insert seafoam version into Pelican context.
    """
    logger.debug(
        "%s Adding Seafoam version (%s) to context." % (LOG_PREFIX, __version__)
    )

    pelican.settings["SEAFOAM_VERSION"] = __version__
