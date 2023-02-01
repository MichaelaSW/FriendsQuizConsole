print("Welcome to my Friends quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play :)")
score = 0

answer = input("Who ran out of their wedding in episode 1? ")
if answer.lower() == "rachel":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What is the first name of Monica's brother? ")
if answer.lower() == "ross":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("How many seasons of Friends is there? ")
if answer == "10":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("Who did Pheobe marry? ")
if answer.lower() == "Mike":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What is Joey's catch phrase? ")
if answer.lower() == "how you doin":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What was Chandler's job? ")
if answer.lower() == "statistical analysis":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What floor is Monica and Rachel's apartment on? ")
if answer.lower() == "third":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What year was the Friend's reunion? ")
if answer.lower() == "2021":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does Joey not share? ")
if answer.lower() == "food":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("Were Ross and Rachel on a break? ")
if answer.lower() == "no":
    print('Correct! suggesting something is not implementing it!!')
    score += 1
else:
    print("Incorrect, come on now we all know they weren't")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/10) * 100) + "%")

