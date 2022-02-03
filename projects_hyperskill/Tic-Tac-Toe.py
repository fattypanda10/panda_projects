def cals():
    col_wise = [[cells_mat[i][j] for i in range(0,3) ] for j in range(0,3)]
    row_wise = [[cells_mat[j][i] for i in range(0,3) ] for j in range(0,3)]
    diag_1 = [[cells_mat[i][j] for i in range(0,3) if i == j ] for j in range(0,3)]
    diag_2 = [[cells_mat[j][i] for i in range(0,3) if i + j == 2 ] for j in range(0,3)]
    empty = [p for p in row_wise if '_' in p]
    x_win = ['X', 'X', 'X']
    x_win_diag = [['X'], ['X'], ['X']]
    o_win = ['O', 'O', 'O']
    o_win_diag = [['O'], ['O'], ['O']] 
    x_win_cond = ((x_win in col_wise) or (x_win in row_wise)) or (x_win_diag == diag_1) or (x_win_diag == diag_2)
    o_win_cond = ((o_win in col_wise) or (o_win in row_wise)) or (o_win_diag == diag_1 or o_win_diag == diag_2)
    
    return x_win_cond, o_win_cond, empty
    
cells = "_________"

cells_mat = [[cells[i] for i in range(3)], 
             [cells[j] for j in range(3,6)], 
             [cells[k] for k in range(6,9)]
             ]
print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
moves = 1
status = True
while status:
    user_input = input("Enter the coordinates: ").split()
    if len(user_input) != 2 or (len(user_input[0]) > 1) or (len(user_input[1]) > 1):
        print("You should enter numbers!")
    else:
        coord_1 = user_input[0]
        coord_2 = user_input[1]
        if (int(coord_1) not in [1,2,3]) or (int(coord_2) not in [1,2,3]):
            print("Coordinates should be from 1 to 3!")
        else:
            coord_1, coord_2 = int(coord_1), int(coord_2)
            coord_1 -= 1
            coord_2 -= 1
            alpha = coord_2
            beta = coord_1
            if alpha == 2: # 1 --> 3
                alpha -= 2
                if cells_mat[alpha][beta] != '_':
                    print("This cell is occupied! Choose another one!")
                else:
                    if moves % 2 != 0:
                        cells_mat[alpha][beta] = 'X'
                        x_win_cond, o_win_cond, empty = cals()
                        moves += 1
                        print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
                        if (len(empty) == 0) and (not x_win_cond) and (not o_win_cond):
                            print("Draw")
                            status = False
                        elif (x_win_cond):
                            print("X wins")
                            status = False
                        elif (o_win_cond):
                            print("O wins")
                            status = False             
                    elif moves % 2 == 0:
                        cells_mat[alpha][beta] = 'O'
                        x_win_cond, o_win_cond, empty = cals()
                        moves += 1
                        print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
                        if (len(empty) == 0) and (not x_win_cond) and (not o_win_cond):
                            print("Draw")
                            status = False
                        elif (x_win_cond):
                            print("X wins")
                            status = False
                        elif (o_win_cond):
                            print("O wins")
                            status = False      
            elif alpha == 0:  # 3 --> 1
                alpha += 2
                if cells_mat[alpha][beta] != '_':
                    print("This cell is occupied! Choose another one!")
                else:
                    if moves % 2 != 0:
                        cells_mat[alpha][beta] = 'X'
                        x_win_cond, o_win_cond, empty = cals()
                        moves += 1
                        print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
                        if (len(empty) == 0) and (not x_win_cond) and (not o_win_cond):
                            print("Draw")
                            status = False
                        elif (x_win_cond):
                            print("X wins")
                            status = False
                        elif (o_win_cond):
                            print("O wins")
                            status = False
                            
                    elif moves % 2 == 0:
                        cells_mat[alpha][beta] = 'O'
                        x_win_cond, o_win_cond, empty = cals()
                        moves += 1
                        print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
                        if (len(empty) == 0) and (not x_win_cond) and (not o_win_cond):
                            print("Draw")
                            status = False
                        elif (x_win_cond):
                            print("X wins")
                            status = False
                        elif (o_win_cond):
                            print("O wins")
                            status = False   
            else:
                if cells_mat[alpha][beta] != '_':
                    print("This cell is occupied! Choose another one!")
                else:
                    if moves % 2 != 0:
                        cells_mat[alpha][beta] = 'X'
                        x_win_cond, o_win_cond, empty = cals()
                        moves += 1
                        print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
                        if (len(empty) == 0) and (not x_win_cond) and (not o_win_cond):
                            print("Draw")
                            status = False
                        elif (x_win_cond):
                            print("X wins")
                            status = False
                        elif (o_win_cond):
                            print("O wins")
                            status = False                  
                    elif moves % 2 == 0:
                        cells_mat[alpha][beta] = 'O'
                        x_win_cond, o_win_cond, empty = cals()
                        moves += 1
                        print(f"""
---------
| {cells_mat[0][0]} {cells_mat[0][1]} {cells_mat[0][2]} |
| {cells_mat[1][0]} {cells_mat[1][1]} {cells_mat[1][2]} |
| {cells_mat[2][0]} {cells_mat[2][1]} {cells_mat[2][2]} |
---------    
""")
                        if (len(empty) == 0) and (not x_win_cond) and (not o_win_cond):
                            print("Draw")
                            status = False
                        elif (x_win_cond):
                            print("X wins")
                            status = False
                        elif (o_win_cond):
                            print("O wins")
                            status = False
