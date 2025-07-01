def get_item_by_name(drive_client, name):
    files = drive_client.list_items()
    for file in files:
        if file["name"] == name:
            return file
    return None
