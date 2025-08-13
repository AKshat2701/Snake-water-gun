# 1 → snake, -1 → water, 0 → gun

computer = -1  # example
you = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
younum = youDict[you]

if computer == younum:
    print("It's a draw")
elif (computer == 1 and younum == -1) or \
     (computer == -1 and younum == 0) or \
     (computer == 0 and younum == 1):
    print("Computer wins")
else:
    print("You win")
