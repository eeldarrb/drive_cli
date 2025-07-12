def handle_upload(session, item_name):
    client = session.client

    client.upload_file(item_name)
