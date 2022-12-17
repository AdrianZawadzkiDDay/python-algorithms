import math

def circle_area(r):
    if r <= 0:
        raise ValueError("Promień ma być dodatni")
    return math.pi * r**2

print(circle_area(4))
print(circle_area(-4))