from .drive_node import DriveNode


def build_drive_tree(client):
    drive_items = client.list_all_items()
    drive_nodes = build_node_map(drive_items)

    root_id = client.get_root_id()
    root_node = DriveNode(root_id, "/", mime_type="application/vnd.google-apps.folder")
    drive_nodes[root_id] = root_node

    link_nodes(drive_items, drive_nodes)
    return root_node


def build_node_map(items):
    return {
        item["id"]: DriveNode(item.get("id"), item.get("name"), item.get("mimeType"))
        for item in items
    }


def link_nodes(items, node_map):
    for item in items:
        node = node_map.get(item.get("id"))
        parent_ids = item.get("parents", [])

        for parent_id in parent_ids:
            parent_node = node_map.get(parent_id)
            if parent_node:
                parent_node.add_child(node)
