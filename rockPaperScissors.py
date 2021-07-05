import random
import time
while True:
    randomNumber = random.randint(1,3)
    if randomNumber==1:
        computerChoice = "Scissors"
    elif randomNumber==2:
        computerChoice = "Paper"
    else:
        computerChoice = "Rock"

    user = input("SC for (Scissors)\nP for (Paper)\nR for (Rock)\nQ for quit\n")
    user.lower()
    if user=="sc" and computerChoice=="Scissors":
        print("Tie")
    elif user=="sc" and computerChoice=="Paper":
        print("Player Won")
    elif user=="sc" and computerChoice=="Rock":
        print("Computer Won")
    elif user=="p" and computerChoice=="Scissors":
        print("Computer Won")
    elif user=="p" and computerChoice=="Paper":
        print("Tie")
    elif user=="p" and computerChoice=="Rock":
        print("Tie")
    elif user=="r" and computerChoice=="Scissors":
        print("Player Won")
    elif user=="r" and computerChoice=="Paper":
        print("Tie")
    elif user=="r" and computerChoice=="Rock":
        print("Tie")
    elif user=="q":
        quit()
    else:
        print("Invalid choice")

    print(f"Computer Choosed {computerChoice}\n")
    time.sleep(1)