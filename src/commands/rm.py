from drive_tree import tree_utils


def handle_rm(session, item_name):
    client = session.client
    curr_dir = session.cwd

    item = tree_utils.get_item_by_name(session, item_name)
    if not item:
        print(f"no such item: {item_name}")
        return

    deleted_item = client.delete_item(item.id)
    if not deleted_item:
        print(f"failed to delete: {item_name}")
        return

    for node in curr_dir.children:
        if node.name == item_name:
            curr_dir.remove_child(node)
            break
