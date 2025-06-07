from commands import command_map


def cli_loop():
    try:
        while True:
            user_line = input("> ").strip()
            if not user_line:
                continue
            cmd, *args = user_line.split()
            if cmd in command_map:
                command_map[cmd](*args)
            else:
                print(f"drive_cli: command not found: {cmd}")
    except KeyboardInterrupt:
        print("\nExiting...")
