class DriveNode:
    def __init__(self, id, name, mime_type):
        self.id = id
        self.name = name
        self.mime_type = mime_type
        self.parent = None
        self.children = []

    def is_folder(self):
        return self.mime_type == "application/vnd.google-apps.folder"

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
            child_node.parent = None

    def detach(self):
        if self.parent:
            self.parent.remove_child(self)
            self.parent = None

    def get_path(self):
        if self.parent is None:
            return "/"
        if self.parent.get_path() == "/":
            return f"/{self.name}"

        return f"{self.parent.get_path()}/{self.name}"
