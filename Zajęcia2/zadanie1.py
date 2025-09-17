class UserNotFoundError(Exception):
    """Wyjątek zgłaszany, gdy użytkownik nie istnieje w systemie."""
    pass


class WrongPasswordError(Exception):
    """Wyjątek zgłaszany, gdy hasło użytkownika jest niepoprawne."""
    pass


class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(f"Użytkownik '{username}' nie istnieje w systemie.")
        if self.users[username] != password:
            raise WrongPasswordError("Podano niepoprawne hasło.")
        return f"Zalogowano pomyślnie jako '{username}'."


auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    print(auth.login("admin", "1234"))
    print(auth.login("unknown", "pass"))
    print(auth.login("user", "wrongpass"))
except Exception as e:
    print(f"Błąd: {e}")
