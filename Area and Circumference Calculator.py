import math

print("Area and Circumference Calculator")

rad = float( input("Please enter the radius value: ") )
area = math.pi*(rad**2)
cir = 2*math.pi*rad

print("Area =", round(area,2))
print("Circumference =", round(cir,2))
