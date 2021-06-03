import random
color=["Red","Green","Yellow","Black","Crimson","Blue","Cyan","Orange","Salmon"]
while True:
    n=random.randint(0,8)
    ran=color[n]
    col=input("Enter a Color : ")
    while True:
        if col == ran:
            print("You won")
            break
        else:
            col=input("Nope,Try again : ")   
    print("Right Guess",ran)
    playagain=input("Wanna Play again ")
    if playagain.lower() == 'no':
        break
print("Nice Game GG!")