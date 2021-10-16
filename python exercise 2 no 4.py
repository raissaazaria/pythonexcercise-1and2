qty = eval(input("Enter the number of packages purchased:"))

retails_price = qty * 99
if qty >= 10 and qty <=19:
    result1 = (10*retails_price/100)
    result_1 = retails_price - result1
    print("Discount amount @10:$", format(result1))
    print("Total amount: $", format(result_1, ".2f"))
elif qty >= 20 and qty <=49:
    result2 =(20*retails_price/100)
    result_2 = retails_price - result2
    print("Discount amount @20%:$", format(result2))
    print("Total amount: $", format(result_2, ".2f"))
elif qty >= 50 and qty <=99:
    result3 = (50 * retails_prices/100)
    result_3 = retails_price - result3
    print("Discount amount @30%:$", format(result3))
    print("Total amount: $", format(result_3, ".2f"))
elif qty >= 100 :
    result4 = (40*retails_price/100)
    result_4 = retails_price - result4
    print("Discount amount @40%:$", format(result4))
    print("Total amount: $", format(result_4, ".2f"))
else:
    print("Discount amount @ 0%: $0.00")
    print("Total amount:$" , format(retails_price, ".2f"))


