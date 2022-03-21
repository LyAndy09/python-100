# This exercise was to understand how variables are stored. The objective of the exercise was to switch inputs a and b and print associated value. 
#E.g. (a = 6, b = 3. which will then print a = 3, b = 6).

a = input ("a: ")
b = intput ("b: ")

c = a
a = b
b = c

print ("a: " + a)
print ("b: " + b)
