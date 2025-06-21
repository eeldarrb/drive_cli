def handle_rm(drive_client, *args):
    drive_client.delete_item(*args)
