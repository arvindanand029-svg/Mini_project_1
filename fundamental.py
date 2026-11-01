name = input("Enter your name: ")
income = float(input("Enter your monthly income : "))
food_expense = float(input("Enter your monthly food expense : "))
travel_expense = float(input("Enter your monthly travel expense : "))
study_expense = float(input("Enter your monthly study expense : "))
mobile_expense = float(input("Enter your monthly mobile expense : "))
other_expense = float(input("Enter your monthly other expense : "))
total_expense = food_expense + travel_expense + study_expense + mobile_expense + other_expense
remaining_income = income - total_expense
if income > 0:
    savings_percentage = (remaining_income / income) * 100
else:
    savings_percentage = 0
if total_expense>0:
    food_percentage = (food_expense / total_expense) * 100
    travel_percentage = (travel_expense / total_expense) * 100
    study_percentage = (study_expense / total_expense) * 100
    mobile_percentage = (mobile_expense / total_expense) * 100
    other_percentage = (other_expense / total_expense) * 100
else:
    food_percentage = 0
    travel_percentage = 0
    study_percentage = 0
    mobile_percentage = 0
    other_percentage = 0
print("n=====MONTHLY EXPENSE REPORT=====")
print(f"Name: {name}")
print(f"Monthly Income: ${income:.2f}")
print(f"Total Expenses: ${total_expense:.2f}")
print(f"Remaining Income: ${remaining_income:.2f}")
print(f"Savings Percentage: {savings_percentage:.2f}%")
print("Expense Breakdown:")
print(f"Food: ${food_expense:.2f} ({food_percentage:.2f}%)")
print(f"Travel: ${travel_expense:.2f} ({travel_percentage:.2f}%)")
print(f"Study: ${study_expense:.2f} ({study_percentage:.2f}%)")
print(f"Mobile: ${mobile_expense:.2f} ({mobile_percentage:.2f}%)")
print(f"Other: ${other_expense:.2f} ({other_percentage:.2f}%)")