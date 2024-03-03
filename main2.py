age = input("Please enter your age: \n")
risk = input("Please enter your risk tolerance as \"low\", \"medium\", or \"high\": \n")
gender = input("Please enter your gender as \"male\" or \"female\": \n")
# switch case for risk tolerance
equities = 100
fixed_income = 0
if gender == "male":
    life_expectancy = 74
elif gender == "female":
    life_expectancy = 80
else:
    life_expectancy = 77
remaining_years = life_expectancy - int(age)
match risk:
    case "low":
        equities -= 35
        fixed_income += 35
    case "medium":
        equities -= 20
        fixed_income += 20
if remaining_years < 15:
    equities -= 50
    fixed_income += 50
elif remaining_years < 20:
    equities -= 45
    fixed_income += 45
elif remaining_years < 25:
    equities -= 40
    fixed_income += 40
elif remaining_years < 30:
    equities -= 35
    fixed_income += 35
elif remaining_years < 35:
    equities -= 30
    fixed_income += 30
elif remaining_years < 40:
    equities -= 25
    fixed_income += 25
elif remaining_years < 45:
    equities -= 20
    fixed_income += 20
elif remaining_years < 50:
    equities -= 15
    fixed_income += 15
elif remaining_years < 55:
    equities -= 10
    fixed_income += 10

        
risk = risk.capitalize()
print( f"\nAge: {age}, Risk Tolerance: {risk}\n Recommended Asset Allocation:\n\n \tEquities: {equities}% \n \tFixed Income: {fixed_income}% \n")