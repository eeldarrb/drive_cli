import io
import os
import mimetypes
from platformdirs import user_downloads_dir
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from utils.retry_on_exception import retry_on_exception


class DriveClient:
    def __init__(self, service):
        self.service = service()

    def get_root_id(self):
        root_id = self.service.files().get(fileId="root").execute()["id"]
        return root_id

    def list_all_files(self):
        files_list = []
        page_token = None

        while True:
            request = self.service.files().list(
                q="trashed=false",
                fields="nextPageToken, files(id, name, mimeType, parents)",
                pageToken=page_token,
            )

            @retry_on_exception()
            def fetchPage():
                return request.execute()

            results = fetchPage()
            files = results.get("files", [])
            files_list.extend(files)
            page_token = results.get("nextPageToken")
            if not page_token:
                break
        return files_list

    @retry_on_exception()
    def create_dir(self, dir_name, folder_id="root"):
        file_metadata = {
            "name": dir_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [folder_id],
        }
        folder = (
            self.service.files()
            .create(body=file_metadata, fields="id, name, mimeType")
            .execute()
        )
        return folder

    @retry_on_exception()
    def delete_file(self, file_id):
        body_value = {"trashed": True}
        deleted_file = (
            self.service.files()
            .update(fileId=file_id, body=body_value, fields="id, name, mimeType")
            .execute()
        )
        return deleted_file

    # TODO: Download directory/multiple files?
    @retry_on_exception()
    def download_file(self, file_id, file_name, file_mimetype):
        download_path = os.path.join(user_downloads_dir(), file_name)
        fh = io.FileIO(download_path, mode="wb")

        # File is a Google Workspace document
        if "vnd.google-apps" in file_mimetype:
            req = self.service.files().export_media(
                fileId=file_id, mimeType="application/pdf"
            )
        else:
            req = self.service.files().get_media(fileId=file_id)

        downloader = MediaIoBaseDownload(fh, req)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        return done

    @retry_on_exception()
    def upload_file(self, file_path, target_dir_id):
        file_type, _ = mimetypes.guess_file_type(file_path)
        file_name = os.path.basename(file_path)
        file_metadata = {"name": file_name, "parents": [target_dir_id]}

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
        return uploaded_file
