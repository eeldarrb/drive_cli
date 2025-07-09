import io
import os
import mimetypes
from platformdirs import user_downloads_dir
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from .drive_utils import get_item_by_name


class DriveClient:
    def __init__(self, service):
        self.service = service()

    def get_root_id(self):
        root_id = self.service.files().get(fileId="root").execute()["id"]
        return root_id

    def list_all_items(self):
        items_list = []
        page_token = None
        while True:
            results = (
                self.service.files()
                .list(
                    q="trashed=false",
                    fields="nextPageToken, files(id, name, mimeType, parents)",
                    pageToken=page_token,
                )
                .execute()
            )
            items = results.get("files", [])
            items_list.extend(items)
            page_token = results.get("nextPageToken")
            if not page_token:
                break
        return items_list

    def list_folder_items(self, folder_id="root"):
        if folder_id == "root":
            q = "'root' in parents and trashed = false"
        else:
            q = f"'{folder_id}' in parents and trashed = false"
        results = (
            self.service.files()
            .list(q=q, fields="files(id, name, mimeType, parents)")
            .execute()
        )
        print(results)
        items = results.get("files", [])
        return items

    def create_dir(self, dir_name, folder_id="root"):
        file_metadata = {
            "name": dir_name,
            "mimeType": "application/vnd.google-apps.folder",
        }
        folder = self.service.files().create(body=file_metadata, fields="id").execute()
        return folder.get("id")

    def delete_item(self, item_name):
        item = get_item_by_name(self, item_name)
        body_value = {"trashed": True}

        if item:
            self.service.files().update(
                fileId=item.get("id"), body=body_value
            ).execute()
        else:
            print(f"Item Not Found: {item_name}")

    # TODO: Download directory/multiple files?
    def download_file(self, file_name):
        item = get_item_by_name(self, file_name)

        if item:
            download_path = os.path.join(user_downloads_dir(), file_name)
            fh = io.FileIO(download_path, mode="wb")

            # File is a Google Workspace document
            if "vnd.google-apps" in item.get("mimeType"):
                req = self.service.files().export_media(
                    fileId=item.get("id"), mimeType="application/pdf"
                )
            else:
                req = self.service.files().get_media(fileId=item.get("id"))

            downloader = MediaIoBaseDownload(fh, req)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Downloading {item.get('name')}: {status.progress() * 100}%")

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
