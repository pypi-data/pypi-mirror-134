import logging
from requests import request
import json

logger = logging.getLogger("ghproject")


def post_request(url: str, data: dict, headers: dict):
    """Send data to GitHub API

    Parameters
    ----------
    url : str
        url to request
    data : dict
        data to be send to url
    headers : dict
        GitHub authentication details

    Returns
    -------
    list
        content of request
    """
    payload = json.dumps(data)

    r = request("POST", url=url, data=payload, headers=headers)

    if r.status_code in [201, 202]:
        logger.debug("Successfully executed the POST request")
        return json.loads(r.content)
    elif r.status_code == 401:
        logger.warning("Status: 401 Unauthorized")
    else:
        logger.warning(json.loads(r.content)["errors"][0]["message"])


def get_request(url: str, headers: dict):
    """Retrieve data from GitHub API

    Parameters
    ----------
    url : str
        url to request
    headers : dict
        authentication details

    Returns
    -------
    list
        content of request
    """

    r = request("GET", url=url, headers=headers)
    if r.status_code == 200:
        logger.debug("Successfully executed the GET request")
        return json.loads(r.content)
    elif r.status_code == 401:
        logger.warning("Status: 401 Unauthorized")
        return None
    else:
        logger.error(json.loads(r.content)["errors"][0]["message"])
        return None


def verify_authentication(url, headers):
    """Verify authentication to GitHub repository

    Parameters
    ----------
    url : str
        url to request
    headers : dict
        authentication details
    """
    r = request("GET", url=url, headers=headers)
    if r.status_code == 200:
        logger.info(f"Authentication successful to {url}")
    elif r.status_code == 401:
        logger.warning("Status: 401 Unauthorized")
    else:
        logger.error(f"Status {r.status_code}, {json.loads(r.content)}")
