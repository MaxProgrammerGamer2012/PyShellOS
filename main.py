import sys
from core import core

class Main:

    def __init__(self, username = "User"):
        self.core = core(username)

    def run(self):
        if self.core.syslang == "eng":
            print(f"Hello, {self.core.username}! Welcome to the system!")
            print("Enter /help to see list of all commands.")
        elif self.core.syslang == "rus":
            print(f"Привет, {self.core.username}! Добро пожаловать в систему!")
            print("Введи /help что-бы увидеть все комманды.")

        while True:
            command = input(">>> ").strip().lower()
            result = self.core.handle_command(command)

            if result == "exit":
                if self.core.syslang == "eng":
                    print("Fine, turning off system. Bye bye!")
                elif self.core.syslang == "rus":
                    print("Окей, выключаю систему. Пока пока!")
                sys.exit()
            elif result == "unknown":
                if self.core.syslang == "eng":
                    print("I don't understand what do you mean. Enter /help, and decide what command you want to use now.")
                elif self.core.syslang == "rus":
                    print("Моя твоя не понимать. Напиши /help что бы решить какую комманду ты хочешь сейчас использовать.")
            elif result:
                print(result)


main = Main("User")
main.run()
