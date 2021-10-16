v=int(input("Enter the plane's take off speed in m/s:"))            #Input
a=float(input("Enter the plane's acceleration m/s**2:"))

formula = (v**2)/(2*a)

print("The minimum runway length needed for this airplane is", formula,"meters" )