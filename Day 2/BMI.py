#Output is the Body Mass Index calculation from a user's weight and height.

#From the assignment
height = input("enter your height in meters: ")
weight = input("enter your weight in kilograms: ")

#My code
BMI = (float(weight)/float(height)**2)
print(int(BMI))