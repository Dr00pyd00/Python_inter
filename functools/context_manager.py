
import time


class Timer():

    start: float
    end: float

    def __init__(self):
        pass 

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end = time.time()
        print(f"temps d'execution => {self.end - self.start}")
        return False 



with Timer():
    print("je commence")
    time.sleep(2)
    print("fini")





