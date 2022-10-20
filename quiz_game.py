print("Welcome to my stocks quiz!")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
print("Okay! Let's play :)")
points = 0
answer = input("What does S&P stand for? ").lower()
if answer == "standard and poors":
    print ("correct!")
    points += 1
else:
    print ("incorrect!")

answer = input("What year did $AAPL IPO? ").lower()
if answer == "1980":
    print ("correct!")
    points += 1
else:
    print ("incorrect!")

answer = input("Is amazon a publicly traded company? ").lower()
if answer == "yes":
    print ("correct!")
    points += 1
else:
    print ("incorrect!")

answer = input("How many shares in ownership are required to sell covered calls?  ").lower()
if answer == "100":
    print ("correct! You have completed this quiz! :) ")
    points += 1
else:
    print ("incorrect!")

print("You got  " + str(points) + " questions correct!")
print("You got  " + str((points/4)*100) + "%")
