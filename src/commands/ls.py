def handle_ls(session):
	for item in session.cwd.children:
		print(item.name)
