def handle_ls(session, *args):
    client = session.client

    items = client.list_folder_items()
    for item in items:
        print(f"{item['name']}")
