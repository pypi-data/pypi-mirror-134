import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def create_http_client():
    """
    :return: an HTTP client that retries on connection errors (and limits redirects). Timeouts can apparently not be
    configured for all requests, so it's not done here.
    """
    retry_strategy = Retry(connect=3, read=0, redirect=5, status=0, other=0)
    adapter = HTTPAdapter(max_retries=retry_strategy)

    client = requests.Session()
    client.mount("https://", adapter)
    client.mount("http://", adapter)

    return client
