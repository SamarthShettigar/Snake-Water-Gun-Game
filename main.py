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
    if(computer==-1 and you==1):
        print("You WIN")
    elif(computer==-1 and you==0):
        print("you LOSE")
    elif(computer==1 and you==0):
        print("you WIN")
    elif(computer==1 and you==-1):
        print("you LOSE")
    elif(computer==0 and you==-1):
        print("you WIN")
    elif(computer==0 and you==1):
        print("you LOSE")
    else:
        print("Something went wrong!!")