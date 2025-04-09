class core:

    def __init__(self, username = "User"):
        self.username = username
        self.commands = ["/help", "/hello", "/exit", "/ver"]

    def handle_command(self, command):
        if command == "/help":
            self.show_help()
        elif command == "/hello":
            self.hello()
        elif command == "/exit":
            return "exit"
        elif command == "/ver":
            self.version()
        else:
            return "unknown"

    def show_help(self):
        print("Here's commands list:")
        print("1. /exit - Exits from system.")
        print("2. /hello - Greets you.")
        print("3. /help - Shows all commands.")
        print("4. /ver - Shows version of system.")

    def hello(self):
        print(f"Hello, {self.username}!")

    def version(self):
        print("Version: PyShellOS One")