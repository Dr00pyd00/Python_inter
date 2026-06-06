
class AppErr(Exception):
    pass 

class AuthErr(AppErr):
    pass 

class UserNotFoundError(AppErr):
    def __init__(self, username):
        self.username = username
        super().__init__(f"utilisateur '{username}' introuvable")


class InvalidPwErr(AuthErr):
    pass 


def login(username: str, password: str):
    if username != "luna":
        raise UserNotFoundError(username=username)
    elif password != "1234":
        raise InvalidPwErr
    print("connexion reussie")

try:
    login("lu", "1234")
except UserNotFoundError:
    print("mauvais user")

try:
    login("luna", "R343")
except InvalidPwErr:
    print("mauvais pw")

try:
    login("luna","1234")
except AppErr:
    print("gobal pb")
