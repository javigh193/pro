#variables y constantes
board_range = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
board = [[0,1,2],[0,0,0],[0,0,0]]
active_player = 1
game_end = False
counter = 0
#movimiento
while not game_end:
    target_position = input('Introduzca el primer movimiento: ')
    if target_position not in board_range:
        print("Posición fuera del tablero")
    else:
        row_index = int(target_position[0]) - 1
        col_index = int(target_position[1]) - 1
        if board[row_index][col_index] != 0:
            print("Posición del tablero ocupada")
        else:
            board[row_index][col_index] = active_player
            if active_player == 1:
                active_player = 2
            else:
                active_player = 1
            counter += 1
#comprobacion ganador
    for row in board:
 # [1, 1, 1] [2, 2, 2] --- todos los demás casos no me dicen quien gana      
        if row[0] == row[1] == row[2]:
            if row[0] == 1:
                gana1
            elif row[0] == 2:
                gana2
            else:
                nogananadie
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 1:
                gana1
            elif board[0][col] == 2:
                gana2
            else:
                nogananadie
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[0][0] == 1:
            gana1
        if board[0][0] == 2:
            gana2
        else:
            nogananadie
#contador hasta 9 para ver si empatan
        game_end = True
    if board[row_index][col_index] == 1:
        print('🔴')
    elif board[row_index][col_index] == 2:
        print('❌')
    else:
        print(board[row_index][col_index])
#tonteria para imprimir
# if board[row_index][col_index] == 1:
#     print('🔴')
# elif board[row_index][col_index] == 2:
#     print('❌')
# else:
#     print(board[row_index][col_index])



       