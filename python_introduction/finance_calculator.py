income =int(input("Enter your monthly income: "))
expense=int(input("Enter your total monthly expenses: "))
savings=income-expense
Projected_Savings = (savings * 12 + (savings * 12 * 0.05))
print("Your monthly savings are", savings)
print("Projected savings after one year, with interest, is:", Projected_Savings)
