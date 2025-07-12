def handle_rm(session, item_name):
    client = session.client
    curr_dir = session.cwd

    for node in curr_dir.children:
        if node.name == item_name:
            curr_dir.remove_child(node)
            break

    client.delete_item(item_name)
