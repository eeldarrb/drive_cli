def handle_rm(session, item_name):
    client = session.client

    client.delete_item(item_name)
