import random

game_board = [' '] * 10
# game_continue = True

def player_one_turn():
    again = True
    while(again):
        while True:
            go = input("X: Where would you like to go? ")
            print('\n')
            try:
                if int(go) < 0 or int(go) > 8:
                    print('Sorry, try a number between 0-8')
                else:
                    break
            except ValueError:
                print("That's not an integer value. Try again.")
        go = int(go)
        if game_board[go] == ' ':
            game_board[go] = 'X'
            again = False
        else:
            print('Sorry, try a different square')

def player_two_turn():
    again = True
    while(again):
        while True:
            go = input("O: Where would you like to go? ")
            print('\n')
            try:
                if int(go) < 0 or int(go) > 8:
                    print('Sorry, try a number between 0-8')
                else:
                    break
            except ValueError:
                print("That's not an integer value. Try again.")
        go = int(go)
        if game_board[go] == ' ':
            game_board[go] = 'O'
            again = False
        else:
            print('Sorry, try a different square')

def display():
    print(('{}|{}|{}\n' * 3).format(*game_board))

def game_over():
    if ((game_board[0] == 'X' and game_board[1] == 'X' and game_board[2] == 'X') or
    (game_board[3] == 'X' and game_board[4] == 'X' and game_board[5] == 'X') or
    (game_board[6] == 'X' and game_board[7] == 'X' and game_board[8] == 'X')):
        print('X wins!')
        return False
    elif ((game_board[0] == 'X' and game_board[3] == 'X' and game_board[6] == 'X') or
    (game_board[1] == 'X' and game_board[4] == 'X' and game_board[7] == 'X') or
    (game_board[2] == 'X' and game_board[5] == 'X' and game_board[8] == 'X')):
        print('X wins!')
        return False
    elif ((game_board[0] == 'X' and game_board[4] == 'X' and game_board[8] == 'X') or
    (game_board[2] == 'X' and game_board[4] == 'X' and game_board[6] == 'X')):
        print('X wins!')
        return False
    elif ((game_board[0] == 'O' and game_board[1] == 'O' and game_board[2] == 'O') or
    (game_board[3] == 'O' and game_board[4] == 'O' and game_board[5] == 'O') or
    (game_board[6] == 'O' and game_board[7] == 'O' and game_board[8] == 'O')):
        print('O wins!')
        return False
    elif ((game_board[0] == 'O' and game_board[3] == 'O' and game_board[6] == 'O') or
    (game_board[1] == 'O' and game_board[4] == 'O' and game_board[7] == 'O') or
    (game_board[2] == 'O' and game_board[5] == 'O' and game_board[8] == 'O')):
        print('O wins!')
        return False
    elif ((game_board[0] == 'O' and game_board[4] == 'O' and game_board[8] == 'O') or
    (game_board[2] == 'O' and game_board[4] == 'O' and game_board[6] == 'O')):
        print('O wins!')
        return False
    return True

def checker(game_board):
    count = 0
    for i in range(len(game_board)):
        if game_board[i] != ' ':
            count += 1
    if count == 8:
        print('CAT: nobody wins!')
        return False
    return True

def game_reset():
    for i in range(len(game_board)):
        game_board[i] = ' '

def main():
    again = True
    while(again):
        display()
        game_continue = True
        g = True
        while(game_continue):
            g = checker(game_board)
            if g != True:
                break
            player_one_turn()
            display()
            g = game_over()
            if g != True:
                break
            player_two_turn()
            display()
            g = game_over()
            if g != True:
                break

        while True:
            again = input('Would you like to play again? (y/n) ').lower()
            print('\n')
            if (again == 'y' or again == 'n'):
                # print('You entered {}, which is a TYPE: {}'.format(again, type(again)))
                break
            else:
                print('Sorry, enter \'y\' or \'n\'')

        if again == 'y'.lower():
            again = True
            game_reset()
            # display()
        elif again == 'n'.lower():
            again = False



main()
