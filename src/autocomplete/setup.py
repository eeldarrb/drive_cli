import gnureadline as readline


def setup_autocomplete(completer, delims=" \t\n;"):
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    readline.set_completer_delims(delims)
