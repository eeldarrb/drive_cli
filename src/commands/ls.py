def handle_ls(session):
    try:
        for item in session.cwd.children:
            print(item.name)
    except Exception as e:
        print(f"[Unexpected Error] Command 'ls' failed: {e}")
