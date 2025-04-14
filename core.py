class core:

    def __init__(self, username="User"):
        self.commands = ["/help", "/hello", "/exit", "/ver", "/lang"]
        self.username = username
        self.syslang = "eng"

    def handle_command(self, command):
        if command == "/help":
            return self.show_help()
        elif command == "/hello":
            return self.hello()
        elif command == "/exit":
            return "exit"
        elif command == "/ver":
            return self.version()
        elif command == "/lang":
            return self.chooselang()
        else:
            return "unknown"

    def show_help(self):
        if self.syslang == "eng":
            return (
                "Here's commands list:\n"
                "1. /lang - Allows you to change the language of the system.\n"
                "2. /exit - Exits from system.\n"
                "3. /hello - Greets you.\n"
                "4. /help - Shows all commands.\n"
                "5. /ver - Shows version of system."
            )
        elif self.syslang == "rus":
            return (
                "Here's commands list:\n"
                "1. /lang - Даёт поменять тебе язык в системе.\n"
                "2. /exit - Выходит из системы.\n"
                "3. /hello - Приветствует тебя.\n"
                "4. /help - Показывает все комманды.\n"
                "5. /ver - Показывает версию системы."
            )

    def hello(self):
        if self.syslang == "eng":
            return f"Hello, {self.username}!"
        elif self.syslang == "rus":
            return f"Привет, {self.username}!"
        

    def version(self):
        if self.syslang == "eng":
            return "Version: PyShellOS Two"
        elif self.syslang == "rus":
            return "Версия: PyShellOS Two"

    def langerror(self):
        if self.syslang == "eng":
            return (
                "I don't understand what language do you mean. Please, try again!\n"
                "Your system language is still English."
            )
        elif self.syslang == "rus":
            return (
                "Я не понимаю о каком языке ты говоришь. Пожалуйста, попробуй ещё раз!\n"
                "Твой системный язык всё ещё Русский."
            )

    def chooselang(self):
        if self.syslang == "eng":
            txt = "Please, choose a language\n"
            txt += f"Your current language: {self.syslang}\n"
            txt += "Variants:\n1. Russian\n2. English\n"
        elif self.syslang == "rus":
            txt = "Пожалуйста, выбери язык\n"
            txt += f"Твой нынешний язык : {self.syslang}\n"
            txt += "Варианты:\n1. Русский\n2. Английский\n"

        print(txt)
        if self.syslang == "eng":
            choice = input("Enter here: ")
        elif self.syslang == "rus":
            choice = input("Вводи сюда:")

        if choice == "English":
            self.syslang = "eng"
            return "You changed your system language to English."
        elif choice == "Russian":
            self.syslang = "rus"
            return "Ты изменил/изменила язык системы на Русский."
        else:
            return self.langerror()

