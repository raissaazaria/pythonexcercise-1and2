import math

g = 9.8
m = eval(input("Enter the mass of the cart(in kg):"))
F = eval(input("Enter the force to push in the cart (in N):"))

sinTh = F/(m*g)

Th = math.asin(sinTh)
th = math.degrees(Th)

print("The angle of the ramp is:","{.1f}" %th)
