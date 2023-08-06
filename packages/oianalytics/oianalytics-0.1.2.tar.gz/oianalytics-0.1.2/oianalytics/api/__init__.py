from typing import Optional

from oianalytics.api._credentials import OIAnalyticsAPICredentials

from oianalytics.api import endpoints

from oianalytics.api._dataframes import (
    get_data_list,
    get_time_values,
    get_batch_types_list,
    get_batch_type_details,
    get_batch_values,
)

# Init
DEFAULT_CREDENTIALS = None


# Default credentials management
def set_default_oianalytics_credentials(
    base_url: str,
    login: Optional[str] = None,
    pwd: Optional[str] = None,
    token: Optional[str] = None,
):
    global DEFAULT_CREDENTIALS
    DEFAULT_CREDENTIALS = OIAnalyticsAPICredentials(
        base_url=base_url, login=login, pwd=pwd, token=token
    )


def get_default_oianalytics_credentials():
    global DEFAULT_CREDENTIALS
    return DEFAULT_CREDENTIALS
