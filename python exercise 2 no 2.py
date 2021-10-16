edge1 = float(input("Enter edge 1:"))
edge2 = float(input("Enter edge 2:"))
edge3 = float(input("Enter edge 3:"))
if (edge1+edge2 > edge3):
    if (edge1+edge3 > edge2):
        if (edge2+edge3 > edge1):
            perimeter = edge1+edge2+edge3
            print ("the perimeter is:", perimeter)

else:
    print ("Perimeter cannot be calculated. Invalid input")