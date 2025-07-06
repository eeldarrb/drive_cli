def handle_mkdir(session, *args):
    client = session.client

    created_folder = client.create_dir(*args)
    print(created_folder)
