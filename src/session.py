def cli_loop():
    try:
        while True:
            user_line = input("> ").strip()
            if not user_line:
                continue
            cmd, *args = user_line.split()

            print(f"cmd {cmd}")
            print(f"args {args}")
    except KeyboardInterrupt:
        print("Exiting...")
