
from dataclasses import dataclass, field
import math


@dataclass 
class Circle:
    radius: float
    area : float = field(init=False)

    def __post_init__(self):
        if self.radius <=0:
            raise ValueError
        self.area = math.pi * (self.radius **2)


c1 = Circle(radius= 10.4)
# c2 = Circle(radius=-3)

print(c1)
