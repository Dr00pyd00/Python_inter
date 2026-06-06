

class MyErr(Exception):
    pass 


def test_err(a: int):
    if a == 0:
        raise MyErr("je suis lerreur de la fonction")


# test_err(0)
#
# try:
#     raise MyErr("hello is ok")
# except MyErr as e:
#     print(f"error custom : {e}")


# on fait de hierachies:

class AppErr(Exception):
    pass 

# puis on creer des sous errors a partir de AppErr:
class DatabaseErr(AppErr):
    pass

class AuthErr(AppErr):
    pass

class NotFoundError(AppErr):
    pass 


try:
    raise AuthErr("pas le bon pw")
except DatabaseErr:
    print("database pb")
except AuthErr:
    print("auth probleme")
except AppErr:
    print("global error")












