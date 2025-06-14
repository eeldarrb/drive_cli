def handle_ls(drive_client, *args):
    items = drive_client.list_items()
    for item in items:
        print(f"{item['name']}")
