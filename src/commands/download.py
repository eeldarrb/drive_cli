def handle_download(session, *args):
    client = session.client

    client.download_file(*args)
