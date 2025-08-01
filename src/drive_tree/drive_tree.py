from .drive_node import DriveNode


def build_drive_tree(client):
    drive_files = client.list_all_files()
    drive_nodes = build_node_map(drive_files)

    root_id = client.get_root_id()
    root_node = DriveNode(root_id, "/", mime_type="application/vnd.google-apps.folder")
    drive_nodes[root_id] = root_node

    link_nodes(drive_files, drive_nodes)
    return root_node


def build_node_map(files):
    return {
        file["id"]: DriveNode(file.get("id"), file.get("name"), file.get("mimeType"))
        for file in files
    }


def link_nodes(files, node_map):
    for file in files:
        node = node_map.get(file.get("id"))
        parent_ids = file.get("parents", [])

        for parent_id in parent_ids:
            parent_node = node_map.get(parent_id)
            if parent_node:
                parent_node.add_child(node)
