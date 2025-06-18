def handle_mkdir(drive_client, *args):
    created_folder = drive_client.create_dir(*args)
    print(created_folder)
