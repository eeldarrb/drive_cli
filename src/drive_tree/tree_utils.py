# TODO: handle getting file from paths
# Only searches in current directory
def get_file_by_name(session, file_name):
    files = session.cwd.children
    for file in files:
        if file.name == file_name:
            return file
    return None
