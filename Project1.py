score = 0

First_name = input("What is your First name?")
Last_name = input("What is your Last name?")
age = input("What is your age?")
print("Hello " + First_name + " " + Last_name)

print("Welcome to a Nation Wide PANDEMIC")
print("Let's see how much you know about Covid-19")

# Question 1
answer1 = input("How many confirmed Covid-19 cases are there in Massachusetts? \na.10,000 \nb.30,000 \nc.over 60,000 \nEnter answer:")
if answer1 == "c" or answer1 == "over 60,000":
    score += 1
    print("That is correct")
    print("score: ", score)

else:
    print("Wrong answer! The correct answer is c.over 60,000")
    print("score: ", score)


# Question 2
answer2 = input("Since the Pandemic how many related deaths have been reported in Massachusetts? \na.Less than 500 \nb.1,000 \nc.over 4,000 \nEnter answer:")
if answer2 == "c" or answer2 == "over 4,000":
    score += 1
    print("Hooray that is correct")
    print("score: ", score)
else:
    print("That is not correct the answer. The correct answer is c.over 4,000")
    print("score: ", score)

# Question 3
answer3 = input("What county has the most reported Covid-19 cases? \na.Middlesex County \nb.Essex County \nc.Suffolk County \nd.Norfolk County \nEnter answer:")
if answer3 == "a" or answer3 == "Middlesex County":
    score += 1
    print("Way to go that is correct")
    print("score: ", score)
else:
    print("Incorrect! The correct answer is a.Middlesex County")
    print("score: ", score)

# Question 4
answer4 = input("What are some ways to protect yourself during this Pandemic? \na.Wear a mask \nb.Social distance \nc.Wash your hands for at least 20 seconds with soap \nd.All of the above \nEnter answer:")
if answer4 == "d" or answer4 == "All the Above":
    score += 1
    print("That is correct")
    print("score: ", score)
else:
    print("Sorry wrong answer. The correct answer is d.All of the above")
    print("score: ", score)

# Question 5
answer5 = input("How much is the fine in Lawrence,MA if you don't wear a mask? \na.$50 \nb.$150 \nc.$300 \nd.$500 \nEnter answer:")
if answer5 == "c" or answer5 == "$300":
    score += 1
    print("That is correct!")
    print("score: ", score)
else:
    print("Wrong answer! The correct answer is c.$300")
    print("score: ", score)

# Question 6
answer6 = input("The city of Lawrence will fine anyone ages ___ and up for not wearing a mask in Lawrence,MA \na.6 \nb.5 \nc.2 \nd.4 \nEnter answer:")
if answer6 == "a" or answer6 == "6":
    score += 1
    print("Correct answer")
    print("score: ", score)
else:
    print("That is not right! The correct answer is a.6")
    print("score: ", score)

# Question 7
answer7 = input("What are the symptoms for Covid-19 \na.Cough \nb.Muscle pain \nc.Shortness of breathe \nd.All of the above \nEnter answer:")
if answer7 == "d" or answer7 == "All of the above":
    score += 1
    print("That is correct")
    print("score: ", score)
else:
    print("Wrong answer! The correct answer is d.All of the above")
    print("score: ", score)

# Question 8
answer8 = input("Who does Covid-19 impact the most? \na.People over the age of 65 \nb.People of all ages \nc.People with underlining conditions \nd.People under 50 \nEnter answer:")
if answer8 == "b" or answer8 == "People of all ages":
    score += 1
    print("That is correct")
    print("You are on a roll")
    print("score: ", score)
else:
    print("That is not correct! The correct answer is b.People of all ages")
    print("score: ", score)

# Question 9
answer9 = input("Is sex recommended during Covid-19? \na.Yes it is ok as long as your wearing a mask. \nb.No sex isn't recommended and you should keep your social distance \nEnter answer:")
if answer9 == "b" or answer9 == "Sex isn't recommended and you should keep your social distance":
    score += 1
    print("That is correct")
    print("score: ", score)
else:
    print("That isn't correct! The correct answer is b.Sex isn't recommend and you should keep your social distance")
    print("score: ", score)

# Question 10
answer10 = input("What businesses are considered essential during this Pandemic? \na.Grocery Stores \nb.Pharmacies \nc.Hospitals \nd.All of the above \nEnter answer:")
if answer10 == "d" or answer10 == "All of the above":
    score += 1
    print("That is the correct answer")
    print("score: ", score)
else:
    print("Wrong answer! The correct answer is d.All of the above")
    print("score: ", score)
if score <=4:
    print("Your total score is:", score, "-Better luck Next Time-")
    print("Thanks for playing")
    print("Remember to Stay Safe and Stay Healthy")
elif score == 5:
    print("Your total score is:", score, "-Not bad-")
    print("Thanks for playing")
    print("Remember to Stay Safe and Stay Healthy")
else:
    print("Your total score is:", score, "-Great Job! I see you know a lot about the Covid-19 Pandemic")
    print("Thanks for playing")
    print("Remember to Stay Safe and Stay Healthy")