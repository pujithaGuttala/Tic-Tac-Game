board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' '
}
player = 1
total_moves = 0
end_check = 0
def check():
    # checking player 1 moves
    # for horizontal rows
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print('Player 1 has won the game')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Player 1 has won the game')
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print('Player 1 has won the game')
        return 1
    # for vertical checks of player 1
    if board['T1'] == 'X' and board['D1'] == 'X' and board['M1'] == 'X':
        print('Player 1 has won the game')
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print('Player 1 has won the game')
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print('Player 1 has won the game')
        return 1
    # for diagonal check of player 1
    if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print('Player 1 has won the game')
        return 1
    if board['T3'] == 'X' and board['M2'] == 'X' and board['D1'] == 'X':
        print('Player 1 has won the game')
        return 1
    # ***** PLAYER 2 CHECKS ************
    # checking player 2 moves
    # for horizontal rows
    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        print('Player 2 has won the game')
        return 1
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
        print('Player 2 has won the game')
        return 1
    if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
        print('Player 2 has won the game')
        return 1
    # for vertical checks of player 2
    if board['T1'] == 'O' and board['D1'] == 'O' and board['M1'] == 'O':
        print('Player 2 has won the game')
        return 1
    if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
        print('Player 2 has won the game')
        return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
        print('Player 2 has won the game')
        return 1
    # for diagonal check of player 2
    if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
        print('Player 2 has won the game')
        return 1
    if board['T3'] == 'O' and board['M2'] == 'O' and board['D1'] == 'O':
        print('Player 2 has won the game')
        return 1
    return 0
print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')
print('*******')

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('-+-+-')
    print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input('PLAYER 1 MOVE')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            # on wrong input z4
            else:
                print('Please enter the correct move')
                continue
        else:
            p2_input = input('PLAYER 2 MOVE')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            # on wrong input z4
            else:
                print('Please enter the correct move')
                continue
            total_moves += 1
    print('***********')
    print()