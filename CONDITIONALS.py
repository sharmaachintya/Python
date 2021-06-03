wt=int(input("Enter your Weight in KG "))
ht=float(input("Enter your height in METERS "))
BMI=(wt/ht*ht)
if BMI <= 18.5:
    print("Underweight")
elif BMI > 18.5 or BMI <= 24.9:
    print("Normal Weight")
elif BMI >24.9 or BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")