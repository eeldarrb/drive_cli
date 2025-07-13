def handle_upload(session, item_name):
    client = session.client

    # TODO: add error message if download fails
    client.upload_file(item_name)
