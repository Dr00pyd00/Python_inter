


def mon_deco(func):
    def wrapper(*args, **kwargs):
        print("func commence")
        func(*args, **kwargs)
        print("func finie")
    return wrapper

@mon_deco
def bonjour():
    print("BONJOUR")


bonjour()

