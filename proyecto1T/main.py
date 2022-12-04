while True:
    # incialización
    board_range = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    active_player = 1
    game_end = False
    turn = 0
    print('¡Es hora de 3 en raya!\nSuerte a ambos jugadores\nPara abortar partida introduzca "abort"')
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            symbol = f'{row_index + 1}{col_index + 1}'
            print(symbol, end='  ')
        print()    
    # bucle principal
    # introducir movimiento
    while not game_end:
        if active_player == 1:
            print('Le toca al jugador 1 🔴')
        else:
            print('Le toca al jugador 2 ❌')
        target_position = input("Introduzca casilla, por ejemplo '11': ")
        if target_position == 'abort':
            break
        if target_position not in board_range:
            print("Esa casilla no pertenece al tablero")
        else:
            row_index = int(target_position[0]) - 1
            col_index = int(target_position[1]) - 1
            if board[row_index][col_index] != 0:
                print("Esa casilla ya está ocupada")
            else:
                board[row_index][col_index] = active_player
                if active_player == 1:
                    active_player = 2
                else:
                    active_player = 1
                turn += 1
        # comprobacion ganador
        for row in board:
            # [1, 1, 1] [2, 2, 2] --- todos los demás casos no me dicen quién gana
            if row[0] == row[1] == row[2] == 1:
                print("¡Gana el jugador 1!")
                game_end = True
            elif row[0] == row[1] == row[2] == 2:
                    print("¡Gana el jugador 2!")
                    game_end = True
        for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col] == 1:
                print("¡Gana el jugador 1!")
                game_end = True
            elif board[0][col] == board[1][col] == board[2][col] == 2:
                print("¡Gana el jugador 2!")
                game_end = True
        if(
            board[0][0] == board[1][1] == board[2][2] == 1
            or board[0][2] == board[1][1] == board[2][0] == 1
        ):
            print("¡Gana el jugador 1!")
            game_end = True
        if(
            board[0][0] == board[1][1] == board[2][2] == 2
            or board[0][2] == board[1][1] == board[2][0] == 2
        ):
            print("¡Gana el jugador 2!")
            game_end = True
        # contador hasta 9 para ver si empatan
        if turn == 9:
            print("Empate")
            game_end = True
        # imprimir el estado del tablero
        for row_index in range(len(board)):
            for col_index in range(len(board)):
                if board[row_index][col_index] == 1:
                    symbol = '🔴'
                elif board [row_index][col_index] == 2:
                     symbol = '❌'
                else:
                    symbol = f'{row_index + 1}{col_index + 1}'
            print(symbol, end='  ')
        print()
    #dar la posibilidad de jugar otra partida
    print('¿Otra partida?')
    new_game = input('¿S/N? ')
    if new_game != 'S':
        break       
print("Gracias por jugar,\n¡hasta pronto!")
