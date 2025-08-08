import random

computer=random.choice([-1,0,1])
user=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[user]

print(f"Your choice: {reverseDict[you]}\n Computer's choice: {reverseDict[computer]} ")

if(computer==you):
    print("It was a Draw")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("You LOSE")
    else:
        print("You WIN")
