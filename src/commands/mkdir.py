def handle_mkdir(session, *args):
    client = session.client
    folder_name = args[0]
    curr_dir = session.cwd.id

    created_folder = client.create_dir(folder_name, curr_dir)
    print(created_folder)
