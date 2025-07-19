from googleapiclient.http import HttpError


def handle_upload(session, file_path):
    client = session.client
    curr_dir = session.cwd

    try:
        uploaded_item = client.upload_file(file_path, curr_dir.id)
        print(f"Successfully uploaded: {uploaded_item.get('name')}")
    except HttpError as e:
        print(f"Failed to upload: {e}")
