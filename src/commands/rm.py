def handle_rm(session, *args):
    client = session.client

    client.delete_item(*args)
