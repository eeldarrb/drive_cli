import os
from .drive_node import DriveNode


class DriveTree:
    def __init__(self, client):
        self.client = client
        self.root = self._build()
        self.cwd = self.root

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

    def cd(self, destination_path):
        self.cwd = self.get_node_by_path(
            self.cwd, destination_path, require_directory=True
        )

    def download(self, file_path):
        file = self.get_node_by_path(self.cwd, file_path)
        self.client.download_file(file.id, file.name, file.mime_type)

    def ls(self, path):
        resolved_node = self.get_node_by_path(self.cwd, path)
        return resolved_node

    def mkdir(self, path):
        *parent_path_segments, dir_name = path.rstrip("/").split("/")
        parent_path = "/".join(parent_path_segments) if parent_path_segments else "."

        parent_node = self.get_node_by_path(self.cwd, parent_path)

        folder_info = self.client.create_dir(dir_name, parent_node.id)
        new_dir = DriveNode(
            folder_info.get("id"),
            folder_info.get("name"),
            folder_info.get("mimeType"),
        )
        parent_node.add_child(new_dir)

    def rm(self, file_path):
        file = self.get_node_by_path(self.cwd, file_path)
        self.client.delete_file(file.id)
        file.detach()

    def upload(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        uploaded_file = self.client.upload_file(file_path, self.cwd.id)
        uploaded_file_node = DriveNode(
            uploaded_file.get("id"),
            uploaded_file.get("name"),
            uploaded_file.get("mimeType"),
        )
        self.cwd.add_child(uploaded_file_node)
        print(f"Successfully uploaded: {uploaded_file.get('name')}")

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
