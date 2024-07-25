import random
'''
1 for snake 
2 for water 
3 for gun
'''

computer=random.choice([1,2,3])
youStr=input("Enter your choice: ")
youDict={"Snake":1,"Water":2,"Gun":3}
reverseDict={1:"Snake",2:"Water",3:"Gun"}

you = youDict[youStr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")
else:
    if(computer==1 and you==2):
        print("You loose!")
    elif(computer==1 and you==3):
        print("You win")
    elif(computer==2 and you==1):
        print("You win")
    elif(computer==2 and you==3):
        print("You loose!")
    elif(computer==3 and you==1):
        print("You loose")
    elif(computer==3 and you==2):
        print("You win")
    else:
        print("Sometihing went wrong!")
