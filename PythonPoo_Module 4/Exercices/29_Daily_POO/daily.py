from rich import print
class Daily:
    def __init__(self, password="leo"):
        self.__secret = []
        self.__password = password.strip()

    def write(self, message):
        if isinstance(message,str) and len(message) > 0:
            self.__secret.append(message.strip())

    def read(self, password = None):
        if password != self.__password:
            raise PermissionError("Password invalid, you cant see the Daily secrets")
        else:
            print(f"[green]Diary unlocked![/]")
            for secret in self.__secret:
                print(f"- {secret}")


    @property
    def password(self):
        raise PermissionError(f"No one can see the password.")
