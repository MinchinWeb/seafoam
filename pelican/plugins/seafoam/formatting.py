import logging

from bs4 import BeautifulSoup

from .constants import LOG_PREFIX

logger = logging.getLogger(__name__)


# def table_fix(html_fragment, settings):
def table_fix(path, context):
    """
    Apply the ".table" class to all HTML tables within generated articles.

    This is so the Bootstrap CSS works as expected.
    """
    REWRITE = False

    with open(path, "r+", encoding=context["SEAFOAM_ENCODING"]) as f:
        soup = BeautifulSoup(f, context["SEAFOAM_PARSER"])

        for table in soup.find_all("table"):
            try:
                if "table" not in table["class"]:
                    table["class"].append("table")
                    REWRITE = True
            except KeyError:
                table["class"] = "table"
                REWRITE = True
            
        if REWRITE:
            logging.debug('%s table fix for "%s"' % (LOG_PREFIX, path))
            f.seek(0)
            f.truncate()
            f.write(str(soup))
