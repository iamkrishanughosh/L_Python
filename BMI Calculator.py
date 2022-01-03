height = float(input("Enter your height in metres : "))
weight = float(input("Enter your weight in kilograms : "))


def bmi_calculator(h, w):
    bmi = w / (h ** 2)
    print(f"\n\nYour BMI is {bmi:1.2f}")
    if bmi <= 18.5:
        print("You are underweight")
    elif 18.5 < bmi <= 25:
        print("You have Normal Weight")
    elif 25 < bmi <= 30:
        print("You are Overweight.\nConsult a Dietitian")
    elif bmi > 30:
        print("You are OBESE.\nDon't eat like a PIG you IDIOT.")


bmi_calculator(height, weight)
