
from dataclasses import dataclass 

@dataclass(frozen=True)
class City:
    name: str
    country: str
    pop: int


c1 = City(name="Paris", country="France", pop=433)


d = {c1 : 98.4}

print(d)
