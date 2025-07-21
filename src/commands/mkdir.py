from drive_tree.drive_node import DriveNode


def handle_mkdir(session, folder_name):
    client = session.client
    curr_dir = session.cwd

    created_folder = client.create_dir(folder_name, curr_dir.id)
    new_dir = DriveNode(
        created_folder.get("id"),
        created_folder.get("name"),
        created_folder.get("mimeType"),
    )
    curr_dir.add_child(new_dir)
