import sys
from core import core

class Main:

    def __init__(self, username="User"):
        self.core = core(username)

    def run(self):
        print(f"Привет, {self.core.username}! Добро пожаловать в систему!")
        print("Напиши /help для списка команд.")

        while True:
            command = input(">>> ").strip().lower()
            result = self.core.handle_command(command)

            if result == "exit":
                print("Fine, leaving system. Bye bye!")
                sys.exit()
            elif result == "unknown":
                print(
                    "I don't understand what do you mean. Enter /help, and decide what command what do you want to use now."
                )
            else:
                print(result)


main = Main("User")
main.run()
