
from dataclasses import dataclass, field



@dataclass 
class Pixel:

    __slots__ = ("x","y","color")

    x: int
    y: int 
    color: str


p1 = Pixel(x=4, y=6, color="blue")
p2 = Pixel(x=9, y=3, color="red")

print(p1)

print(p1.x)
print(p1.color)

p1.a = 10

