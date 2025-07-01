import io
import os
import mimetypes
from platformdirs import user_downloads_dir
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


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

    def create_dir(self, dir_name, folder_id="root"):
        file_metadata = {
            "name": dir_name,
            "mimeType": "application/vnd.google-apps.folder",
        }
        folder = self.service.files().create(body=file_metadata, fields="id").execute()
        return folder.get("id")

    def delete_item(self, name):
        # TODO: Abstract name to id conversion into util function
        files = self.list_items()
        match = None
        for file in files:
            if file["name"] == name:
                match = file
        body_value = {"trashed": True}
        if match:
            self.service.files().update(
                fileId=match.get("id"), body=body_value
            ).execute()
        else:
            print(f"File Not Found: {name}")

    # TODO: Download directory/multiple files?
    def download_file(self, name):
        # TODO: Abstract name to id conversion into util function
        files = self.list_items()
        match = None
        for file in files:
            if file["name"] == name:
                match = file
        if match:
            file_id = match.get("id")
            download_path = os.path.join(user_downloads_dir(), name)
            fh = io.FileIO(download_path, mode="wb")

            # File is a Google Workspace document
            if "vnd.google-apps" in match.get("mimeType"):
                req = self.service.files().export_media(
                    fileId=file_id, mimeType="application/pdf"
                )
            else:
                req = self.service.files().get_media(fileId=file_id)

            downloader = MediaIoBaseDownload(fh, req)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Downloading {name}: {status.progress() * 100}%")

    def upload_file(self, file_path):
        file_type, _ = mimetypes.guess_file_type(file_path)
        file_name = os.path.basename(file_path)
        file_metadata = {"name": file_name}

        # TODO: allow tab completion for file uploading?
        media = MediaFileUpload(file_path, mimetype=file_type)
        uploaded_file = (
            self.service.files()
            .create(
                body=file_metadata,
                media_body=media,
            )
            .execute()
        )
        if uploaded_file:
            print(f"Successfully uploaded file: {uploaded_file.get('name')}")
