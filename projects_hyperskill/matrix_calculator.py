## List Reversal
def list_reverse(a):
    list_rev = []
    for i in range(0, len(a)):
        alpha = a[-1* (i + 1)]
        list_rev.append(alpha)
    return list_rev


## Matrix Print Function - "Properly"
def mat_print(a):
    mat = a
    g = ' '
    print("\nThe result is:\n")
    for i in mat:
        for j in i:
            if j < 0:
                if (j - int(j) != 0):
                    print(f"{j + 0:.4f}{g}", end = '\t')
                else:
                    print(f"{int(j + 0)}{g*2}", end = '\t')
            elif j >= 0:
                if (j - int(j) != 0):
                    print(f"{g}{j + 0:.4f}{g}", end = '\t')
                else:
                    print(f"{g}{int(j + 0)}{g*4}", end = '\t')
        print('\n')

## "The Inverter" - calculate the inverse of matrix
def mat_inverse(a, b):
    mat = a
    determinant = b
    minors = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            minor = [ [mat[p][q] for q in range(len(mat[0])) if q != j] for p in range(len(mat)) if p != i]
            minors.append(minor)
            
    values = [ mat_determinant(minors[alpha]) for alpha in range(len(minors))]
    mat_values = []
    mat_ele = []
    z = 0
    for x in range(0, len(values), len(mat)):
        while z != len(mat):
            y = values[x + z]
            mat_ele.append(y)
            z += 1
        mat_values.append(mat_ele)
        z = 0
        mat_ele = []
                    
    mat_cofac = []
    mat_cofac_temp = []
    for m in range(0, len(mat_values)):
        for n in range(0, len(mat_values[0])):
            beta = mat_values[m][n] * ((-1) ** (m + n))
            mat_cofac_temp.append(beta)
        mat_cofac.append(mat_cofac_temp)
        mat_cofac_temp = []
       
    mat_cofac_trans = mat_transposer(1, mat_cofac)
    mat_inverse = [ [ ((1 / determinant) * j) for j in i ] for i in mat_cofac_trans ]
    return mat_inverse

## "The Determinantor" - calculate the determinant of matrix
def mat_determinant(a):
    mat = a
    if (len(mat) and len(mat[0])) == 1:
        mat_val = mat[0][0]
        return mat_val
    elif (len(mat) and len(mat[0])) == 2:
        mat_val = ((mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0]))
        return mat_val
    else:
        minors = []
        for j in range(len(mat[0])):
            minor = [ [mat[p][q] for q in range(len(mat[0])) if q != j] for p in range(len(mat)) if p != 0]
            minors.append(minor)
        mat_req = [ (mat[0][alpha] * ((-1) ** alpha) * mat_determinant(minors[alpha])) for alpha in range(len(mat[0])) ]
        mat_val = sum(mat_req)
        return mat_val

## "The Transposer" - calculate different types of transpose for a matrix
def mat_transposer(a, b):
    
    def norm_trans(mat):
        mat_transpose = [ [i[j] for i in mat] for j in range(len(mat[0])) ]
        return mat_transpose
    
    def side_trans(mat):
        alpha = verti_trans(mat)
        beta = hori_trans(alpha)
        return norm_trans(beta)
    
    def verti_trans(mat):
        mat_transpose = []
        for i in mat:
            mat_transpose.append(list_reverse(i))
        return mat_transpose
    
    def hori_trans(mat):
        return (list_reverse(mat))
    
    option = a
    mat = b
    
    if option == 1:
        mat_req = norm_trans(mat)
    elif option == 2:
        mat_req = side_trans(mat)
    elif option == 3:
        mat_req = verti_trans(mat)
    elif option == 4: 
        mat_req = hori_trans(mat)
    
    return mat_req

## Matrix Input and Parsing
def mat_input(rows):
    
    row = 0
    mat = []
    while row < rows:
        rowy = input().split()
        # line = [float(i) if '.' in i else int(i) for i in rowy]
        line = [float(i) for i in rowy]
        mat.append(line)
        row += 1
    return mat

# Matrices Addition
def mat_add():
    count = 0
    dims = []
    while count < 2:
        
        if count == 0:
            size_1 = input("Enter size of first matrix: ").split()
            dims.append([int(size_1[0]), int(size_1[1])])
            print("\nEnter first matrix:")
            mat_1 = mat_input(dims[0][0])
            
        elif count == 1:
            size_2 = input("Enter size of second matrix: ").split()
            dims.append([int(size_2[0]), int(size_2[1])])
            print("\nEnter second matrix:")
            mat_2 = mat_input(dims[1][0])
            
        count += 1
    
    mat_add = []
    add_row = []
    if dims[0] == dims[1]:
        for i in range(0, len(mat_1)):
            for j in range(0, len(mat_1[0])):
                sumy = mat_1[i][j] + mat_2[i][j]
                add_row.append(sumy)
            mat_add.append(add_row)
            add_row = []
    else:
        print("The operation cannot be performed.")
    
    mat_print(mat_add)
        
## Multiplication of Matrix with Constant
def mat_mul_const():
    dims = []
    size = input("Enter size of matrix: ").split()
    dims.append([int(size[0]), int(size[1])])
    print("\nEnter matrix:")
    mat = mat_input(dims[0][0])
    const = float(input("Enter constant: "))
    mat_const_mul = [ [(const * j) for j in i] for i in mat ]
    mat_print(mat_const_mul)

## Multiplication of Matrices
def mat_mul():
    count = 0
    dims = []
    while count < 2:
        
        if count == 0:
            size_1 = input("Enter size of first matrix: ").split()
            dims.append([int(size_1[0]), int(size_1[1])])
            print("\nEnter first matrix:")
            mat_1 = mat_input(dims[0][0])
            
        elif count == 1:
            size_2 = input("Enter size of second matrix: ").split()
            dims.append([int(size_2[0]), int(size_2[1])])
            print("\nEnter second matrix:")
            mat_2 = mat_input(dims[1][0])
            
        count += 1
        
    dim_1 = dims[0]
    dim_2 = dims[1]
    mat_mul = []
    ele_mat= []
    if dims[0][1] == dims[1][0]:
        ind_1 = 0
        ind_2 = 0
        while ind_1 < dim_1[0]:
            chosen_row = [ mat_1[ind_1][i] for i in range(dim_1[1]) ]
            while ind_2 < dim_2[1]:
                chosen_col = [ mat_2[j][ind_2] for j in range(dim_2[0]) ]
                ele_list = [ chosen_row[i] * chosen_col[i] for i in range(dim_1[1]) ]
                ele_mat.append(sum(ele_list))
                ind_2 += 1
            mat_mul.append(ele_mat)
            ele_mat = []
            ind_2 = 0
            ind_1 += 1
    else:
        print("The operation cannot be performed.")
        
    mat_print(mat_mul)
        
## Transpose of Matrix
def mat_trans():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
""")
    option = int(input("Your choice: "))    
    dims = []
    size = input("Enter size of matrix: ").split()
    dims.append([int(size[0]), int(size[1])])
    print("\nEnter matrix:")
    mat = mat_input(dims[0][0])
    mat_req = mat_transposer(option, mat)
    mat_print(mat_req)
    
## Determinant of Matrix
def mat_det():
    dims = []
    size = input("Enter size of matrix: ").split()
    dims.append([int(size[0]), int(size[1])])
    print("\nEnter matrix:")
    mat = mat_input(dims[0][0])
    
    if dims[0][0] == dims[0][1]:
        mat_deter = mat_determinant(mat)
    else:
        print("The operation cannot be performed.")
        
    print("The result is:")
    print(mat_deter)
    
## Inverse of Matrix
def mat_inv():
    dims = []
    size = input("Enter size of matrix: ").split()
    dims.append([int(size[0]), int(size[1])])
    print("\nEnter matrix:")
    mat = mat_input(dims[0][0])
    determinant = mat_determinant(mat)
    if determinant != 0:
        mat_req = mat_inverse(mat, determinant)
        mat_print(mat_req)
    else:
        print("This matrix doesn't have an inverse.")
    

## Main Program - "Matrix Calculator"
print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit  
""")

choice = int(input("Your choice: "))

while choice != 0:
    if choice == 1:
        mat_add()
    elif choice == 2:
        mat_mul_const()
    elif choice == 3:
        mat_mul()
    elif choice == 4:
        mat_trans()
    elif choice == 5:
        mat_det()
    elif choice == 6:
        mat_inv()
        
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit  
""")
    choice = int(input("Your choice: "))
