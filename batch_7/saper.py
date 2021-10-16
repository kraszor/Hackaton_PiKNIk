import random
number_of_mines = "10"
size_x = "0"
size_y = "0"
print((int(size_x) < 1 and int(size_x) > 15))
while (size_x.isdigit() is False) or (int(size_x) < 1 or int(size_x) > 15):
    size_x = input("Choose number of rows: ")
while (size_y.isdigit() is False) or (int(size_y) < 1 or int(size_y) > 15):
    size_y = input("Choose number of columns: ")
while (number_of_mines.isdigit() is False) or (int(number_of_mines) <= 0 or int(number_of_mines) > int(size_x)*int(size_y)):
    number_of_mines = input(f"choose number of mines: ")

size_x = int(size_x)
size_y = int(size_y)
number_of_mines = int(number_of_mines)
board = [["0" for x in range(size_x)] for y in range(size_y)]
table_of_possible_neighbours = [[0 for x in range(size_x)] for y in range(size_y)]
playboard = [[" " for x in range(size_x)] for y in range(size_y)]
mine_coordinates = []
while number_of_mines > 0:
    row = random.randint(0, size_x-1)
    column = random.randint(0, size_y-1)
    if  board[row][column] != "*":
        board[row][column] = "*"
        number_of_mines -= 1
        mine_coordinates.append((row, column))


for row in range(0, size_x):
    for column in range(0, size_y):
        possible_neighbour_rows = [row, row + 1, row - 1]
        possible_neighbour_columns = [column, column + 1, column - 1]  # determine possible neighbors of cell
        for check_row in  possible_neighbour_rows:
            if check_row < 0 or check_row >= size_x:
                possible_neighbour_rows.pop(possible_neighbour_rows.index(check_row))
        for check_column in possible_neighbour_columns:
            if check_column < 0 or check_column >= size_y:
                possible_neighbour_columns.pop(possible_neighbour_columns.index(check_column))
        table_of_possible_neighbours[row][column] = (possible_neighbour_rows, possible_neighbour_columns)
        if board[row][column] == "*":
            for neighbour_row in possible_neighbour_rows:
                for neighbour_column in possible_neighbour_columns:
                    if board[neighbour_row][neighbour_column] != "*":
                        board[neighbour_row][neighbour_column] = str(int(board[neighbour_row][neighbour_column]) + 1)
input_row = ""
input_column = ""
while True:
    for x in range(0, size_x):
        print(board[x])
    for x in range(0, size_x):
        print(playboard[x])
    while not input_row.isdigit() or (int(input_row) < 0 and int(input_row) > size_x-1):
        input_row = input(f"enter correct row by typing number from range 0 to {size_x-1}: ")
    while not input_column.isdigit() or (int(input_column) < 0 and int(input_column) > int(input_row) > size_y-1):
        input_column = input(f"enter correct column by typing number from range 0 to {size_y-1}: ")
    if playboard[int(input_row)][int(input_column)] != " ":
        print("you already defused this tile! Choose another one")
    elif board[int(input_row)][int(input_column)] == "*":
        print(f"you lose, {(len(mine_coordinates))} left")
        break
    elif board[int(input_row)][int(input_column)] == "0":
        playboard[int(input_row)][int(input_column)] = "-"
        possible_neighbour_rows = table_of_possible_neighbours[int(input_row)][int(input_column)][0]
        possible_neighbour_columns = table_of_possible_neighbours[int(input_row)][int(input_column)][1]
        for neighbour_row in possible_neighbour_rows:
            for neighbour_column in possible_neighbour_columns:
                if board[neighbour_row][neighbour_column] == "0":
                    playboard[neighbour_row][neighbour_column] = "-"
                else:
                    playboard[neighbour_row][neighbour_column] = board[neighbour_row][neighbour_column]
    else:
        playboard[int(input_row)][int(input_column)] = board[int(input_row)][int(input_column)]
    if sum(x.count(' ') for x in playboard) == len(mine_coordinates):
        print("YOU WON, CONGRATULATIONS!!!")
        break
    input_row = ""
    input_column = ""



