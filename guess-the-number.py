import random

hidden=random.randint(1,1000)


print("this is hidden number game, you have 10 chancces to find the hidden number")
print("Gess the number between 1 TO 1000")

i=10
while (i>=0):
    print("guess the number")
    num=int(input())
    if num==hidden:
        print("you win")
    elif i==0:
        print("You Lost")
        print(f"Hidden number was {hidden}")
        break
    elif num>hidden:
        print('you entered a large number,and u have',i,'chances left')
    elif num<hidden:
        print('you entered a small number,and u have',i,'chances left')

    else:
        print("enter a valid number")
    i=i-1;
print("Thanks for playing this game plz leave feedback too.")
