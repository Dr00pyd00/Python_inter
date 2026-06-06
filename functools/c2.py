
import time 

class MyOpen:

    def __init__(self, filename, interaction):
        self.filename = filename
        self.interaction = interaction 
        self.file = None
        self.start = 0
        self.end = 0


    def __enter__(self):
        self.file = open(self.filename, self.interaction)
        self.start = time.time()
        return self.file 


    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end = time.time()
        if self.file:
            self.file.close()
        print(f"with total time => {self.end - self.start}")
        return False

with MyOpen("data.txt", "w") as file:
    file.write("Hello\n")





# sans class :

from contextlib import contextmanager

@contextmanager
def timer2(): 
    start = time.time()
    yield
    end = time.time()
    print(f"temps d'exec de timer2 : {end -start}")


with timer2():
    print("t2 commence ...")
    time.sleep(1)
    print("t2 fini...")



