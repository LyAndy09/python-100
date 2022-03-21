#Code will display how much time we have left from an arbitrarily chosen 90 years.

#From Assignment
age = input("what is your current age?")

#My code
days = 90 * 365 - int(age) * 365

weeks = 90 * 52 - int(age) * 52

months = 90 * 12 - int(age) * 12

print(f"You have {days} days , {weeks} weeks, {months} months left.")