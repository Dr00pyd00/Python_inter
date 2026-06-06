from functools import wraps 



def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"nom de la f: {func.__name__}")
        print(f"doc de la f: {func.__doc__}")
        print(f"appel de {func.__name__} avec args={args} kwargs={kwargs}")
        func(*args, **kwargs)
    return wrapper


@log_call
def bonjour(name: str):
    """Une Fonction qui dit bonjour"""
    print(f"Bonjour {name}")


bonjour("koko")


