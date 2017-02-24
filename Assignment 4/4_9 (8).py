import math

n = int(input("Enter radius: "))

def areaOfCircle(r):
    a = math.pi*(r**2)
    return round(a,2)

print(areaOfCircle(n))
