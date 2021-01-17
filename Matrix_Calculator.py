#Matrix Calculator.
#Used if-else,List,list comprehension ,loop . 

# while(1) loop for running program again and again
while(1):
    # Menue 
    print("----------MENUE--------------")
    print("1 : Matrix Addtion ")
    print("2 : Matrix Subtraction ")
    print("3 : Matrix Multiplication ")
 #Choose menue 
    choose= int(input("Which Operation you want ?\nInput 1 - 3 : "))
# Checking conditon which Operation want user 
    if(choose == 1):
        # Matrix Row and Coloum
        print("-----------Matrix Addtion----------------")
        row=int(input("Enter the Row of the Matrix : "))
        col=int(input("Enter the Coloum of the Matrix : "))

        # used List comprehension for tkaing input and store data in Matrix_1 and Matrix_2
        Matrix_1 =[[int(input("Input Data for First Matrix "))for j in range(col)] for i in range(row)]
        Matrix_2 =[[int(input("Input Data for Second Matrix "))for j in range(col)] for i in range(row)]
#printing first matrix 
        print("Frist Matrix :\n")
        for i in range(row):
            for j in range(col):
                print(Matrix_1[i][j],end="  ")
            print()
#printing second matrix 
        print("Second Matrix :\n")
        for i in range(row):
            for j in range(col):
                print(Matrix_1[i][j],end="  ")
            print()

        # Another Empty list for store result 
        result=[[0 for j in range(col)] for i in range(row)]
        # Addtion Matrix_1 + Matrix_2 
        print("---------Result----------")
        for i in range(row):
            for j in range(col):
                result[i][j]=Matrix_1[i][j]+Matrix_2[i][j]
        # printing result 
        for i in range(row):
            for j in range(col):
             print(result[i][j],end=" ")
            print()

    if(choose == 2):
        # Matrix Row and Coloum
         print("---------------Matrix Subtraction-----------------")
         row=int(input("Enter the Row of the Matrix : "))
         col=int(input("Enter the Coloum of the Matrix : "))
        # used List comprehension for tkaing input and store data in Matrix_1 and Matrix_2
         Matrix_1 =[[int(input("Input Data for First Matrix "))for j in range(col)] for i in range(row)]
         Matrix_2 =[[int(input("Input Data for Second Matrix "))for j in range(col)] for i in range(row)]
         
        # Another Empty list for store result 
         result=[[0 for j in range(col)] for i in range(row)]
        # Subtraction Matrix_1 - Matrix_2 
         for i in range(row):
             for j in range(col):
                 result[i][j]=Matrix_1[i][j]-Matrix_2[i][j]
        
        #printing firs matrix 
         print("Frist Matrix :\n")
         for i in range(row):
             for j in range(col):
                 print(Matrix_1[i][j],end="  ")
             print()
         print("Second Matrix : \n")
         for i in range(row):
             for j in range(col):
                 print(Matrix_2[i][j])
             print()
        # Printing result
         print("----------Result-----------")
         for i in range(row):
             for j in range(col):
                 print(result[i][j],end=" ")
             print()

    # matrix multipication
    if(choose==3):
        print("---------------Matrix Multiplication-----------------")
        #input row and column for matrix_1 and matrix_2
        matrix_1_Row=int(input("Enter the First Matrix Row :"))
        matrix_1_Col=int(input("Enter the First Matrix Column :"))
        matrix_2_Row=int(input("Enter the Second Matrix Row :"))
        matrix_2_Col=int(input("Enter the Second Matrix Column :"))
        #checking condition matrix_1_row and matrix_2_col is same or not.
        #  if its not same than it will ask for again input 
        while(matrix_1_Row != matrix_2_Col):
            print("Error ! First Matrix Row and Second Matrix Column is not same.Please try again")
            matrix_1_Row=int(input("Enter the First Matrix Row :"))
            matrix_1_Col=int(input("Enter the First Matrix Column :"))
            matrix_2_Row=int(input("Enter the Second Matrix Row :"))
            matrix_2_Col=int(input("Enter the Second Matrix Column :"))
        # used List comprehension for tkaing input and store data in Matrix_1 and Matrix_2
        matrix_1=[[int(input("Enter Data for Frist Matrix :")) for j in range(matrix_1_Col)]for i in range(matrix_1_Row)]
        matrix_2=[[int(input("Enter Data for Second Matrix :")) for j in range(matrix_2_Col)]for i in range(matrix_2_Row)]
        # multiplication matrix_1 and matrix_2 and store in result variable
        # used List comprehension  store data in result list . initiali result list is 0 or empty
        result=[[0 for j in range(matrix_2_Col)] for i in range(matrix_1_Row)]
        #logic for matrix multiplication 
        for i in range(matrix_1_Row):
            for j in range(matrix_2_Col):
                for k in range(matrix_2_Row):
                    result[i][j]=result[i][j] + matrix_1[i][k]*matrix_2[k][j]
        
        #printing first Matrix
        print("First Matrix :\n")

        for i in range(matrix_1_Row):
            for j in range(matrix_1_Col):
                print(matrix_1[i][j],end="  ")
            print()
        #printing second matrix 
        print("Second Matrix")
        for i in range(matrix_2_Row):
            for j in range(matrix_2_Col):
                print(matrix_2[i][j],end="  ")
            print()
        #printing after calculation
        print("----------Reuslt----------")
        for i in range(matrix_1_Row):
            for j in range(matrix_2_Col):
                print(result[i][j],end=" ")
            print()



         




