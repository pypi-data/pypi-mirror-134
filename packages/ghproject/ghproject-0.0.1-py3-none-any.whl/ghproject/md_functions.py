import os
import glob
import logging
import frontmatter

logger = logging.getLogger("ghproject")


def load_markdown_files(path: str):
    """Load markdown files for uploading as issues

    Parameters
    ----------
    path : str
        Path to markdown files
    """

    files = glob.glob(f"{path}/*.md")
    issues = []

    if not files:
        logger.warning(f"No markdown files found in {path}")
    else:

        for file in files:
            with open(file, "r") as f:
                issues.append(frontmatter.load(f))
                logger.info(
                    f"Issue '{issues[-1]['title']}' imported from file '{os.path.basename(file)}'"
                )

    return issues
