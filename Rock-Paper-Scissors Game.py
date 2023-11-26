import random 

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    total_games = 5
    user_score = 0
    computer_score = 0

    for game_num in range(1, total_games + 1):
        print(f"\nGame {game_num} - Rock, Paper, Scissors")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

        user_choice = input("Enter your choice (1-4): ").lower()

        if user_choice == '4':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        if user_choice in ['1', '2', '3']:
            user_choice = choices[int(user_choice) - 1]
            result = determine_winner(user_choice, computer_choice)
            print(f"\nYou chose {user_choice.capitalize()}. Computer chose {computer_choice.capitalize()}.")
            print(result)

            if 'win' in result:
                user_score += 1
            elif 'lose' in result:
                computer_score += 1

            print(f"Scores - You: {user_score}  Computer: {computer_score}")

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

    print("\nGame Over!")
    if user_score > computer_score:
        print("Congratulations! You won the majority of the games.")
    elif user_score < computer_score:
        print("Better luck next time! The computer won the majority of the games.")
    else:
        print("It's a tie! Both you and the computer won an equal number of games.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
