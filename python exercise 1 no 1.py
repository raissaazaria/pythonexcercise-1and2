x1 = eval(input("Enter the x-coordinate for point 1 : "))                                                            #Enter statetment for each coordinate
y1 = eval(input("Enter the y-coordinate for point 1 : "))
x2 = eval(input("Enter the x-coordinate for point 2 : "))
y2 = eval(input("Enter the y-coordinate for point 2 : "))

slope = (y2 - y1) / (x2 - x1)                                                                                        #Enter formula based on the question

print("The slope that connects", (x1, y1), "and", (x2, y2), "is", format(slope, '.5f'))                              #Print the the slope and the rounding
