import random

keep_playing = True

computer_wins = 0
human_wins = 0

while keep_playing:
    answers = ["rock", "paper", "scissors"]
    computer_answer = random.choice(answers)
    print("Want to play or not?")
    human_answer = input()
    human_answer = human_answer.lower()

    if human_answer == "quit":
        break

    if human_answer not in answers:
        print("Not a valid answer")
        exit()

    print(f"Computer played {computer_answer}")

    if computer_answer == human_answer:
        print("Nobody wins")
    elif computer_answer == "rock" and human_answer == "scissors":
        print("Computer Wins!")
        computer_wins += 1
    elif computer_answer == "paper" and human_answer == "rock":
        print("Computer Wins")
        computer_wins += 1
    elif computer_answer == "scissors" and human_answer == "paper":
        print("Computer wins")
        computer_wins += 1
    else:
        print("Human Wins!")
        human_wins += 1
print("Thanks for Playing")