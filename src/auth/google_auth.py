from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]
API_SERVICE_NAME = "drive"
API_VERSION = "v3"


def get_auth_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(host="localhost", port=0)
    service = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
    return service
