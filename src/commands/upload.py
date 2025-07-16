def handle_upload(session, file_path):
    client = session.client
    curr_dir = session.cwd

    uploaded_item = client.upload_file(file_path, curr_dir.id)
    if not uploaded_item:
        print(f"Failed to upload: {uploaded_item.get('name')}")
        return
    else:
        print(f"Successfully uploaded: {uploaded_item.get('name')}")
