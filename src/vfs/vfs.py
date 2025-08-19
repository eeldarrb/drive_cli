class VFS:
    def __init__(self, client, node_cls):
        self.client = client
        self._node_cls = node_cls
        self.root = self.__build()
        self.cwd = self.root

    def __build(self):
        all_files = self.client.list_all_files()
        root_id = self.client.get_root_id()

        # Create dictionary of nodes using files
        drive_nodes = {
            file["id"]: self._node_cls(
                file.get("id"), file.get("name"), file.get("mimeType")
            )
            for file in all_files
        }
        drive_nodes[root_id] = self._node_cls(
            root_id, "/", mime_type=self._node_cls.folder_mimetype
        )

        # Link nodes together into tree
        for file in all_files:
            node = drive_nodes.get(file.get("id"))
            parent_ids = file.get("parents", [])
            for parent_id in parent_ids:
                parent_node = drive_nodes.get(parent_id)
                if parent_node:
                    parent_node.add_child(node)
        return drive_nodes[root_id]

    def cd(self, path):
        self.cwd = self._resolve_node_by_path(path, require_dir=True)

    def ls(self, path):
        file_node = self._resolve_node_by_path(path)
        return file_node

    def mkdir(self, path):
        *parent_path_segments, dir_name = path.rstrip("/").split("/")
        parent_path = "/".join(parent_path_segments) if parent_path_segments else "."

        parent_node = self._resolve_node_by_path(parent_path)

        file_info = self.client.create_dir(dir_name, parent_node.id)
        file_node = self._node_cls(
            file_info.get("id"),
            file_info.get("name"),
            file_info.get("mimeType"),
        )
        parent_node.add_child(file_node)

    def rm(self, path):
        file_node = self._resolve_node_by_path(path)
        self.client.delete_file(file_node.id)
        file_node.detach()

    def download(self, path):
        file_node = self._resolve_node_by_path(path)
        self.client.download_file(file_node.id, file_node.name, file_node.mime_type)

    def upload(self, local_path):
        file_info = self.client.upload_file(local_path, self.cwd.id)
        file_node = self._node_cls(
            file_info.get("id"),
            file_info.get("name"),
            file_info.get("mimeType"),
        )
        self.cwd.add_child(file_node)
        return file_node

    # TODO: add require file enforcement to args
    def _resolve_node_by_path(self, path, allow_partial=False, require_dir=False):
        path_segments = path.split("/")
        is_relative = path_segments[0] != ""
        curr_node = self.cwd if is_relative else self.root

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
                    if allow_partial:
                        break
                    raise FileNotFoundError(path)
                curr_node = found_node

        if require_dir and not curr_node.is_folder():
            raise NotADirectoryError(path)
        return curr_node
