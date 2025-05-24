aactual_cost = float(input("Enter the actual Product Price: "))
sale_amount = float(input("Enter the Sale Amount: "))
if (sale_amount > aactual_cost):
    amount = sale_amount - aactual_cost
    print("total profit ={θ}".format(amount))
else:
    print("No profit!!!!!!!")