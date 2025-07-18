class DriveNode:
    def __init__(self, id, name, mime_type):
        self.id = id
        self.name = name
        self.mime_type = mime_type
        self.parent = []
        self.children = []

    def is_folder(self):
        return self.mime_type == "application/vnd.google-apps.folder"

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def remove_child(self, child_node):
        self.children.remove(child_node)
        child_node.parent = None
