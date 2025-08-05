from .drive_node import DriveNode


class DriveTree:
    def __init__(self, client):
        self.client = client
        self.root = self._build()

    def _build(self):
        all_files = self.client.list_all_files()
        root_id = self.client.get_root_id()

        # Create dictionairy of DriveNodes using files
        drive_nodes = {
            file["id"]: DriveNode(
                file.get("id"), file.get("name"), file.get("mimeType")
            )
            for file in all_files
        }
        drive_nodes[root_id] = DriveNode(
            root_id, "/", mime_type="application/vnd.google-apps.folder"
        )

        # Link DriveNodes together into tree
        for file in all_files:
            node = drive_nodes.get(file.get("id"))
            parent_ids = file.get("parents", [])
            for parent_id in parent_ids:
                parent_node = drive_nodes.get(parent_id)
                if parent_node:
                    parent_node.add_child(node)
        return drive_nodes[root_id]

    # TODO: add require file enforcement to args
    def get_node_by_path(self, starting_node, path, require_directory=False):
        path_segments = path.split("/")
        is_relative = path_segments[0] != ""
        curr_node = starting_node if is_relative else self.root

        for path_segment in path_segments:
            if path_segment in ["", "."]:
                continue
            elif path_segment == "..":
                if curr_node.parent is None:
                    raise FileNotFoundError(path)
                curr_node = curr_node.parent
            else:
                found_node = next(
                    (
                        child_node
                        for child_node in curr_node.children
                        if child_node.name == path_segment
                    ),
                    None,
                )
                if found_node is None:
                    raise FileNotFoundError(path)
                curr_node = found_node

        if require_directory and not curr_node.is_folder():
            raise NotADirectoryError(path)
        return curr_node
