import random 

computer = random.choice([1,2,3])
print("To play this game you have to Choose :\nSnake\nWater\nGun")
yourchoice = input("Enter Your Choice :").lower()
Dict = {"snake":1,"water":2,"gun":3}
ReverseDict = {1:"snake",2:"water",3:"gun"}
print(f"You Choose {yourchoice.capitalize()}\nComputer Choose {ReverseDict[computer]}")
try:
    if(computer == Dict[yourchoice]):
        print("Its a Draw!")

    else:
        if(computer == 1 and Dict[yourchoice] == 2):
            print("You Lose!")

        elif(computer == 1 and Dict[yourchoice] == 3):
            print("You Win!")

        elif(computer == 2 and Dict[yourchoice] == 1):
            print("You Win!")

        elif(computer == 2 and Dict[yourchoice] == 3):
            print("You Lose!")

        elif(computer == 3 and Dict[yourchoice] == 1):
            print("You Lose!")

        elif(computer == 3 and Dict[yourchoice] == 2):
            print("You Win!")

        else:
            print("Somthing went Wrong!")

except:
    print("Invalid choice! Please enter Snake, Water, or Gun.")



