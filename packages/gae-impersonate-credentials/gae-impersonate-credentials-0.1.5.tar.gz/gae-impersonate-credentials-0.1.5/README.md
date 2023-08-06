# gae-impersonate-credentials

Get an GCP Credentials instance

App runs in GCP, return None for use Application Default Credentials(ADC).
When runs in local, impersonate requested service account by ADC.
(In local environment, ADC is developer's own google account that signed in with `gcloud auth application-default login` in normal usage.)

If use this function on Cloud Functions Python 3.9 Runtime, this function cannot detect actual run environment, because not supplied to `GOOGLE_CLOUD_PROJECT` or `GCP_PROJECT` environment variables.
You need to supply these value in deploy Cloud Functions deployment parameter or set `is_run_on_gcp` parameter in this function.

## Example usage

```
from gae_credentials import get_credentials
from google.cloud import ndb


credentials = get_credentials(
    service_account='example@appspot.gserviceaccount.com',
    scopes=[
      'https://www.googleapis.com/auth/datastore'
    ]
)

client = ndb.Client(credentials=credentials)
```
