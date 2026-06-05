
from dataclasses import dataclass, field


@dataclass 
class Book:
    title: str
    author: str
    pages: int
    tags: list = field(default_factory=list)


l1 = Book(title="hp", author="truc", pages=100)
l2 = Book(title="hp", author="truc", pages=100)

print(l1)
print(l2)

print(l1 == l2)


