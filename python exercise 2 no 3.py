flag = True

temp = eval(input("Enter the temperature in Fahrenheit:"))
while(flag):
    if (-58 < temp < 41):
        flag = False
        break
    else:
        print("Temperature must be between -58F and 41F")
        temp = eval(input("Please re - enter temperature in Fahrenheit:"))

flag= True

wind= eval(input("Enter the wind speed miles per hour:"))
while(flag):
    if (wind >= 2):
        formula = 35.74 + (0.6215 * temp) - (35.75 * wind**0.16) + 0.4275 * temp * (wind**0.16)
        print("The wind chill index is","{:,.3f}".format(formula))
        flag= False
        break
    else:
        print("Speed must be greater than or equal to 2")
        wind = eval(input("Please re-enter the wind speed miles per hour:"))


