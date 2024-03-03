# Robo Advisor Project - FIN4450 Foundations of FinTech.
# Authors: Daniel Gonzalez, Jacob Voelker, Jason Griller, and Sam Nazari


# Our Robo Advisor will provide a recommendation for an investment portfolio for a user based on their risk tolerance and life expectancy.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    age = int(request.form["age"])
    risk = request.form["risk_tolerance"]
    gender = request.form["gender"]
    # switch case for risk tolerance
    equities = 100
    fixed_income = 0
    if gender == "male":
        life_expectancy = 74
    elif gender == "female":
        life_expectancy = 80
    else:
        life_expectancy = 77
    remaining_years = life_expectancy - age
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
    gender = gender.capitalize()

    stats = f"Age: {age},\t Risk Tolerance: {risk},\t Gender: {gender}" 
    allocation = f"Equities: {equities}% \n Fixed Income: {fixed_income}% \n"
    return render_template('result.html', stats=stats, allocation=allocation)



if __name__ == '__main__':
    app.run(debug=True)
