#Body Mass Index 2.0, goal of this assignment was to understand the function of elif statements.

#Assignment code
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#My Code
BMI = round(float(weight)/(float(height)**2))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
