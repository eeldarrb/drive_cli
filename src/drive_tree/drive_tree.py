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
