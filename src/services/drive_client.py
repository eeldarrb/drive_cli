class DriveClient:
    def __init__(self, service):
        self.service = service()

    def list_items(self, folder_id="root"):
        if folder_id == "root":
            q = "'root' in parents and trashed = false"
        else:
            q = f"'{folder_id}' in parents and trashed = false"
        results = (
            self.service.files().list(q=q, fields="files(id, name, mimeType)").execute()
        )
        items = results.get("files", [])
        return items
