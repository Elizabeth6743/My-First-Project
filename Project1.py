import random
First_name = input("What is your First name?")
Last_name = input("What is your Last name?")

print("Hello " + First_name + " " + Last_name)
print("Welcome to a Nation Wide PANDEMIC")
response = input("Do you know how many confirmed Covid-19 cases there are in Massachusetts?")
answer = input("Enter yes or no")
if answer == "yes":
    print("I see you know what is going on in the world")
elif answer == "no":
    print("I guess you don't know what is going on in the world today")
    print("There is a PANDEMIC going on in this world")
    print("There are over 60,000 cases in Massachusetts.")

question = input("Do you know how many death realated Covid=19 cases there are in Massachusetts?")
answer = input("yes or no")
if answer == ("yes"):
    print("That is sad there are over 3,000 deaths in Massachusetts")
    print("We have to do better to protect ourselves.")
elif answer == "no":
    print("There are so many people dying from this virus there are over 3,000 deaths in Massachusetts")
    print("We need to take the precautions to protect ourselves")

response = input("Here are some ways you can protect yourself during this pandemic")
a = []
b = []
c = []
a = "Wash your hands for at least 20 seconds and sanitize them when you are done."
b = "Wear your mask every time you step out of your house."
c = "Give people space and stand back at least 6 feet."
print(a)
print(b)
print(c)

question = input("Do you know how much the fine is in Lawrence,MA if you don't wear a mask?")

num1 = "$1000"
num2 = "$500"
num3 = "$300"
print(num1, num2, num3)
