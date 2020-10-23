# [✅] 1: print an empty field
cells = []
# construct the cells of the tic-tac-toe board
for index in range(9):
    cells.append('_')

# print(cells)

# Print Field
print("---------")
print("|" + " " + cells[0] + " " + cells[1] + " " + cells[2] + " " + "|")
print("|" + " " + cells[3] + " " + cells[4] + " " + cells[5] + " " + "|")
print("|" + " " + cells[6] + " " + cells[7] + " " + cells[8] + " " + "|")
print("---------")

"""
[] 2: Creates a game loop
where the program asks the user to
enter the cell coordinates,
analyzes the move for correctness
and shows a field with the changes
if everything is ok.
"""
# keep track of who's turn it is
# set to true since x play first
is_x_turn = True

# game loop
while True:
    # [✅] x starts the game and o plays second, turns alternate between x an o

    # user move, and analyzing the move

    # used to indicate to loop if input is right
    is_input_good = False
    converted_user_move = int()
    # ask user about next move and receive user input
    while not is_input_good:
        user_move = input("Enter the coordinates: > ")

        # check if the input is numbers
        if user_move.split()[0].isdigit() and user_move.split()[1].isdigit():
            # print("You entered numbers")
            # check if the numbers are from 1 to 3
            if 1 <= int(user_move.split()[0]) <= 3 and 1 <= int(user_move.split()[0]) <= 3:
                # print(" input is within range ")
                # check if cell chosen is empty
                """
                convert 
                map inputs
                (1, 3) (2, 3) (3, 3)
                (1, 2) (2, 2) (3, 2)
                (1, 1) (2, 1) (3, 1)
                
                to cell indexes
                0 1 2
                3 4 5
                6 7 8
        
                so that
                (1, 3) = 0, (2, 3) = 1, (3, 3) = 2,
                (1, 2) = 3, (2, 2) = 4,  (3, 2) = 5,
                (1, 1) = 6, (2, 1) = 7, (3, 1) = 8
                
                then check is cell is that user choose to move to is empty          
                """
                # convert input to cell indexes
                if int(user_move.split()[0]) == 1 and int(user_move.split()[1]) == 3:
                    converted_user_move = 0
                if int(user_move.split()[0]) == 2 and int(user_move.split()[1]) == 3:
                    converted_user_move = 1
                if int(user_move.split()[0]) == 3 and int(user_move.split()[1]) == 3:
                    converted_user_move = 2
                if int(user_move.split()[0]) == 1 and int(user_move.split()[1]) == 2:
                    converted_user_move = 3
                if int(user_move.split()[0]) == 2 and int(user_move.split()[1]) == 2:
                    converted_user_move = 4
                if int(user_move.split()[0]) == 3 and int(user_move.split()[1]) == 2:
                    converted_user_move = 5
                if int(user_move.split()[0]) == 1 and int(user_move.split()[1]) == 1:
                    converted_user_move = 6
                if int(user_move.split()[0]) == 2 and int(user_move.split()[1]) == 1:
                    converted_user_move = 7
                if int(user_move.split()[0]) == 3 and int(user_move.split()[1]) == 1:
                    converted_user_move = 8

                # check if cell index is empty
                if cells[converted_user_move] != '_':
                    print("This cell is occupied! Choose another one!")
                else:

                    """
                     join cells back into a string
                    and put into string variable
                    """
                    cells_string = "".join(cells)
                    updated_cell_string = ""
                    print()
                    for cell_string_index, cell_string_value in enumerate(cells_string):
                        if cell_string_index == converted_user_move:
                            if is_x_turn:
                                # this is x's turn, place an x
                                updated_cell_string += 'X'
                                # print("adding an x")
                                # print("value of the updated cells string", updated_cell_string)
                                # set is_x_turn to False for the next turn, so that O may go
                                is_x_turn = False
                            else:
                                # this is O's turn
                                updated_cell_string += 'O'

                                # print("adding an o")
                                # print("value of the updated cells string", updated_cell_string)

                                # set is_x_turn to True for next turn, so that x may go
                                is_x_turn = True
                        else:
                            updated_cell_string += cell_string_value
                            # print("not add an x or o to the cell string")
                            # print("value of the updated cells string", updated_cell_string)
                    """
                    break the string back into a list
                    and assign to old list cells
                    cells = cells_string.split(" ")
                    """
                    # print move before
                    # print("cells before turn", cells)
                    # update the board with the new move.
                    cells = list(updated_cell_string)
                    # print move after
                    # print("cells after turn", cells)

                    # exit the loop
                    is_input_good = True
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    # output field:
    # print the field updated
    print("---------")
    print("|" + " " + cells[0] + " " + cells[1] + " " + cells[2] + " " + "|")
    print("|" + " " + cells[3] + " " + cells[4] + " " + cells[5] + " " + "|")
    print("|" + " " + cells[6] + " " + cells[7] + " " + cells[8] + " " + "|")
    print("---------")

    # check game state
    # Find the state in which the game is at the moment and print it. Possible states:
    is_empty_cells = False
    is_x_three_in_a_row = False
    is_o_three_in_a_row = False

    # used to track number of X's on the board
    num_x = 0
    # used to track number of O's on the board
    num_o = 0
    # number of x's and o's in the current game state:
    for symbol in cells:
        if symbol == 'X':
            num_x += 1
        elif symbol == 'O':
            num_o += 1

    # Game not finished, when no side has a three in a row but there are still empty cells

    # check for empty cells
    if "_" in cells:
        is_empty_cells = True
        print(cells)
        # print("there are empty cells")
    else:
        is_empty_cells = False
       #  print("there are no empty cells")

    # need to be more explicit
    # update condition to check each index individually
    # for example instead of
    # if index1 and index2 and index 3 == "something"
    # (logic if this this and that == something do something) seems to not work
    # need to be in the form
    # if index1 == "something" and index2 == "something" and index3 == "something"
    # (logic if this equal something and this equals something and that equals something then do something )
    # Check for horizontal three in a row for X or O

    # first row horizontal.
    if cells[0] == 'X' and cells[1] == 'X' and cells[2] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, first row horizontal.")

    if cells[0] == 'O' and cells[1] == 'O' and cells[2] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, first row horizontal.")

    # second row horizontal.
    if cells[3] == 'X' and cells[4] == 'X' and cells[5] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, second row horizontal.")

    if cells[3] == 'O' and cells[4] == 'O' and cells[5] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, second row horizontal.")

    # third row horizontal.
    if cells[6] == 'X' and cells[7] == 'X' and cells[8] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, third horizontal.")

    if cells[6] == 'O' and cells[7] == 'O' and cells[8] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, third row horizontal.")

    # Check for vertical three in a row for X or O
    # first column vertical.
    if cells[0] == 'X' and cells[3] == 'X' and cells[6] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, first column vertical.")

    if cells[0] == 'O' and cells[3] == 'O' and cells[6] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, first column vertical.")

    # second column vertical.
    if cells[1] == 'X' and cells[4] == 'X' and cells[7] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, second column vertical.")

    if cells[1] == 'O' and cells[4] == 'O' and cells[7] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, second column vertical.")

    # third column vertical.
    if cells[2] == 'X' and cells[5] == 'X' and cells[8] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, third column vertical.")

    if cells[2] == 'O' and cells[5] == 'O' and cells[8] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, third column vertical.")
        # print('v3')

    # Check for diagonal three in a row for X or O

    # thinking about vertical win states
    # 1st diagonal
    # x - -
    # - x -
    # - - x
    # indexes 0,4,8

    # 2nd diagonal
    # - - x
    # - x -
    # x - -
    # indexes 2,4,6

    # only two diagonal win states
    # 1st diagonal.
    if cells[0] == 'X' and cells[4] == 'X' and cells[8] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, first diagonal")

    if cells[0] == 'O' and cells[4] == 'O' and cells[8] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, first diagonal")

    # 2nd diagonal
    if cells[2] == 'X' and cells[4] == 'X' and cells[6] == 'X':
        is_x_three_in_a_row = True
        # print("x got three in a row, second diagonal")

    if cells[2] == 'O' and cells[4] == 'O' and cells[6] == 'O':
        is_o_three_in_a_row = True
        # print("o got three in a row, second diagonal")

    # break of of game loop when x or o wins or there is a draw

    # if empty cells is true and there is not three in a row either x or 0 then print (game not finished)
    # if is_empty_cells and (not(is_o_three_in_a_row or is_x_three_in_a_row)):
        # print("Game not finished")

    # "Draw" when no side has a three in a row and there are no empty cells left;
    # if empty cells is false and there is not three in a row for either x or o then print draw
    if not is_empty_cells and (not(is_o_three_in_a_row or is_x_three_in_a_row)):
        print("Draw")
        # break out of the game loop
        break

    # "X wins" when the field has three Xs in a row;
    # if x has three in a row and o does not then x wins
    if is_x_three_in_a_row:  # and (not is_o_three_in_a_row):
        # print("X wins")
        # break out of the game loop
        break
        # print(bool(is_x_three_in_a_row))
    # "O wins" when the field has three Os in a row;
    # if o has three in a row and x does not then o wins
    if is_o_three_in_a_row:  # and not is_x_three_in_a_row:
        # print("O wins")
        # break out of the game loop
        break
        # (bool(is_o_three_in_a_row))
    # "Impossible" when the field has three Xs in a row as well as three Os in a row.
    # Or the field has a lot more Xs that Os or vice versa (if the difference is 2 or more, should be 1 or 0).
    # if (is_x_three_in_a_row and is_o_three_in_a_row) or (num_o - num_x >= 2 or num_x - num_o >= 2):
        # print("Impossible")
        # break
# output the final result after the end of the game.
print("---------")
print("|" + " " + cells[0] + " " + cells[1] + " " + cells[2] + " " + "|")
print("|" + " " + cells[3] + " " + cells[4] + " " + cells[5] + " " + "|")
print("|" + " " + cells[6] + " " + cells[7] + " " + cells[8] + " " + "|")
print("---------")
if is_x_three_in_a_row:
    print("X wins")
elif is_o_three_in_a_row:
    print("O wins")
else:
    print("Draw")
