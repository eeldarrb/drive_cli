# TODO: handle getting item from paths
# Only searches in current directory
def get_item_by_name(session, item_name):
    items = session.cwd.children
    for item in items:
        if item.name == item_name:
            return item
    return None
