def handle_download(session, item_name):
    client = session.client

    client.download_file(item_name)
