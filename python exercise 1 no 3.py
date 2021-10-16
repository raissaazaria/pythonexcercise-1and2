sub_total =eval(input("Enter the subtotal:$"))
tip_amount =eval(input("Enter the tip amount(as a%):"))
tip = (tip_amount/100)*sub_total
total = sub_total + tip

print("Subtotal: $", "{:,.2f}".format(sub_total))
print ("Tip:$", "{:,.2f}".format(tip))
print("Total:$", "{:,.2f}". format(total))