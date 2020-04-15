# создаем матрицу 8х8 и заполняем ее 0
chess_board = [[0 for j in range(8)] for i in range(8)]
flag = True
# заполняем матрицу и ставим 1 в указанные координаты
for i in range(8):
    row, col = [int(i) - 1 for i in input().split()]
    chess_board[row][col] = 1

# проверяем матрицу
for i in range(len(chess_board)): # перебираем строки
    for j in range(len(chess_board[i])): # перебираем столбцы
        if chess_board[i][j] == 1: # находим клетку с ферзем
            for h in range(1, 8): #
                if chess_board[i - h][j] == 1: # перебираем все клетки по вертикали
                    flag = False
                if chess_board[i][j - h] == 1: # перебираем все клетки по горизонтали
                    flag = False
                if chess_board[i - h][j - h] == 1: # перебираем все клетки по диагонали
                    flag = False

if flag:
    print('YES')
else:
    print('NO')