def handle_upload(session, *args):
    client = session.client

    client.upload_file(*args)
