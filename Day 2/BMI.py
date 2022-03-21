#Output is the Body Mass Index calculation from a user's weight and height.

height = input("enter your height in meters: ")
weight = input("enter your weight in kilograms: ")

BMI = (float(weight)/float(height)**2)
print(int(BMI))