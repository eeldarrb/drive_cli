from drive_tree import tree_utils


def handle_rm(session, item_name):
    client = session.client
    curr_dir = session.cwd

    item = tree_utils.get_item_by_name(session, item_name)
    if not item:
        raise FileNotFoundError(item_name)

    client.delete_item(item.id)

    for node in curr_dir.children:
        if node.name == item_name:
            curr_dir.remove_child(node)
            break
