import os
from typing import List
from typing import Optional

from google.auth import default as app_default_credentials
from google.auth import impersonated_credentials
from google.auth.credentials import Credentials


def _is_run_on_gcp():
    return 'GOOGLE_CLOUD_PROJECT' in os.environ or 'GCP_PROJECT' in os.environ


def get_credentials(service_account: str,
                    scopes: List[str],
                    lifetime: int = 3600,
                    is_run_on_gcp: Optional[bool] = None
                    ) -> Optional[Credentials]:
    """Get an GCP Credentials instance
    App runs in GCP, return None for use Application Default Credentials(ADC).
    When runs in local, impersonate requested service account by ADC.
    (In local environment, ADC is developer's own google account that signed in with `gcloud auth application-default login` in normal usage.)

    If use this function on Cloud Functions Python 3.9 Runtime, this function cannot detect actual run environment
    because not supplied to GOOGLE_CLOUD_PROJECT or GCP_PROJECT environment variable.
    You need to supply these value in deploy Cloud Functions or set is_run_on_gcp parameter in this function.

    :param service_account: Service account to impersonate access.
    :param scopes: Requested api scopes
    :param lifetime: Credential life time
    :param is_run_on_gcp: set to True in run in GCP, if not supplied or passed None, use auto detection from environment variable.
    :return: return None on runs in GCP, otherwise Credentials object.
    """
    if is_run_on_gcp is None and _is_run_on_gcp() or is_run_on_gcp:
        return None
    source_credentials, default_project_id = app_default_credentials()
    target_credentials = impersonated_credentials.Credentials(
        source_credentials=source_credentials,
        target_principal=service_account,
        target_scopes=scopes,
        lifetime=lifetime)
    return target_credentials
