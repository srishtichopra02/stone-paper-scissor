

player = input("enter your choice from",)
player2= input("enter your choice",)
if player==player2:
    print("do it again")
elif player=="rock":
    if player2=="scissor":
        print("player wins")
    else:
        print("you lose")
elif player=="rock":
    if player2=="paper":
        print("you lose")
    else:
        print("player2 wins")
elif player=="paper":
     if player2=="rock":
         print("player wins")
     else:
        print("you lose")
elif player=="paper":
    if player2=="scissor":
        print("player2 wins")
    else:
        print("you lose")
elif player=="scissor":
    if player2=="rock":
         print("player2 wins")
    else:
        print("you lose")
elif player=="scissor":
    if player2=="paper":
         print("player wins")
    else:
         print("you lose")
else:
     ("not a correct option")
