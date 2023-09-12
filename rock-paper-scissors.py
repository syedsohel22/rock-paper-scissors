import random


def get_user_choice():
    # Ask the user for their choice (rock, paper, or scissors) and return it
    while True:
        user_choice = input(
            "Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    # Select a random choice for the computer (rock, paper, or scissors) and return it
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    # Compare the two choices and determine the winner
    # Return 'user', 'computer', or 'draw'
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'


def update_score(winner, scores):
    # Update the score based on the winner and return the updated score dictionary
    if winner == 'user':
        scores['user'] += 1
    elif winner == 'computer':
        scores['computer'] += 1
    else:
        scores['draw'] += 1
    return scores


def display_score(scores):
    # Display the current score (number of rounds user won, computer won, and draws)
    print(
        f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draw']}")


def play_again():
    # Ask the user if they want to play again
    # Return True if they want to play again, otherwise return False
    return input("Do you want to play again? (yes/no): ").strip().lower() == 'yes'


def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chooses: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        scores = update_score(winner, scores)

        display_score(scores)

        if not play_again():
            break

    print("Thank you for playing Rock, Paper, Scissors!")


if __name__ == "__main__":
    main()
