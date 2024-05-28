# write 'hello world' to the console
print('hello world')

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.

# write a function that takes two strings as input and returns the winner of the game
# if the first string wins, return 'first'
# if the second string wins, return 'second'
# if it's a tie, return 'tie'
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return 'tie'
    if player1 == 'rock' and player2 == 'scissors':
        return 'first'
    if player1 == 'scissors' and player2 == 'paper':
        return 'first'
    if player1 == 'paper' and player2 == 'rock':
        return 'first'
    return 'second'

def main():
    player1_score = 0
    player2_score = 0
    while True:
        player1 = input('Player 1, choose rock, paper, or scissors: ').lower()
        if player1 not in ['rock', 'paper', 'scissors']:
            print('Invalid option')
            continue
        player2 = input('Player 2, choose rock, paper, or scissors: ').lower()
        if player2 not in ['rock', 'paper', 'scissors']:
            print('Invalid option')
            continue
        winner = rock_paper_scissors(player1, player2)
        if winner == 'first':
            player1_score += 1
            print('Player 1 wins!')
        elif winner == 'second':
            player2_score += 1
            print('Player 2 wins!')
        else:
            print('It\'s a tie!')
        print(f'Player 1 score: {player1_score}')
        print(f'Player 2 score: {player2_score}')
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again != 'yes':
            break

if __name__ == '__main__':
    main()

    