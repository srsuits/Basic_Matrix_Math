# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:38:19 2021

@author: shelb
"""

import numpy as np

# Get size dimensions of vectors from user input
def get_size(num_matrix):
    '''
    
    Returns
    -------
    int
        size of matrices
    '''
    
    row1 = input("Enter the number of rows in matrix 1: ")
    column1 = input("Enter the number of columns in matrix 1: ")
    
    dimensions = [[row1, column1]]
    
    if num_matrix == 2:
        row2 = input("Enter the number of rows in matrix 2: ")
        column2 = input("Enter the number of columns in matrix 2: ")
        dimensions.append([row2, column2])
        
    return dimensions


# Get vector(s) from user input
def get_matrix(num_m, sizes):
    '''
    
    Parameters
    ----------
    num_m : int
        number of matrices (1 or 2)
    size_m : nested list
        dimensions of matrices
    Returns
    -------
    matrices: nested list
        matrices from user inputs
    '''
    # Create list to hold return vectors
    matrices = []
    
    # For each matrix
    for matrix in range(0, num_m):
        
        # Create empty list for individual matrix
        matrix_list = []
        

        print("ENTER THE VALUE FOR EACH POSITION IN MATRIX " + str(matrix + 1))
        # Rows
        for i in range(0, int(sizes[matrix][0])):
                
            rows = []
            # Columns
            for j in range(0,int(sizes[matrix][1])):
                    
                # Get the element
                element = input("row " + str(i + 1) + " column " + str(j + 1) + ":  ")
                
                # Add element to row
                rows.append(float(element))
            
            # Add row to matrix
            matrix_list.append(rows)
                                
        # Add finish matrix to matrices 
        matrices.append(matrix_list)
        
    return(matrices)
            
            

# Perform the operation chosen by user
def do_math(text):
    '''
    Parameters
    ----------
    text : string
        user input to choose which vector operation to perform
    Returns
    -------
    new_vec : np array or number
        result of vector operation
    '''
    # Ignore all capitalization
    text = text.lower()
    
    
    if text == 'addition':
        
        # Get the matrix sizes
        matrix_size = get_size(2)
        
        # Get matrices from user input
        matrices = get_matrix(2, matrix_size)

        # Separate nested lists and cast to np array
        mat1 = np.array(matrices[0])
        mat2 = np.array(matrices[1])
        
        # Math
        new_mat = mat1 + mat2
        
    elif text == 'subtraction':
        
        # Get the matrix sizes
        matrix_size = get_size(2)
        
        # Get matrices from user input
        matrices = get_matrix(2, matrix_size)

        # Separate nested lists and cast to np array
        mat1 = np.array(matrices[0])
        mat2 = np.array(matrices[1])
        
        # Math
        new_mat = mat1 - mat2

    elif text == 'hadamard multiplication':
        
        # Get the matrix sizes
        matrix_size = get_size(2)
        
        # Get matrices from user input
        matrices = get_matrix(2, matrix_size)

        # Separate nested lists and cast to np array
        mat1 = np.array(matrices[0])
        mat2 = np.array(matrices[1])
        
        # Math        
        new_mat = mat1 * mat2
        
    elif text == 'scalar multiplication':
        
        # Get the matrix size
        matrix_size = get_size(1)
        
        # Get matrix and scalar from user input
        scalar = float(input("Enter the scalar to multiply your vector by: "))
        matrices = get_matrix(1, matrix_size)
        
        # Separate nested list and cast to np array
        mat1 = np.array(matrices[0])
        
        # Math
        new_mat = mat1 * scalar
        
    elif text == 'matrix multiplication':
        
        # Get the matrix sizes
        matrix_size = get_size(2)
        
        # Get matrices from user input
        matrices = get_matrix(2, matrix_size)

        # Separate nested lists and cast to np array
        mat1 = np.array(matrices[0])
        mat2 = np.array(matrices[1])
        
        # Math
        new_mat = np.dot(mat1,mat2)
        
#    elif text == 'constant addition':
#        # Get vector and constant from user input
#        constant = float(input("Enter the constant to add to your vector: "))
#        vec1 = np.array(get_vectors(1, vec_size)[0])
#        
#        # Math
#        new_vec = vec1 + constant
    else:
        print("\nERROR: incorrect input \nEnter only letters \nChoose one of the options listed\n")
        return -1
    # Return the result of the vector operation
    return new_mat

    

result = np.array([])

while result.size == 0:
    # Get operation from user input
    print("Operations: \n\t Addition \n\t Subtraction \n\t Hadamard Multiplication \n\t Scalar Multiplication \n\t Matrix Multiplication ")
    operation = input("Choose a matrix operation from the list above: ")
    result = do_math(operation)

    
print("!!!!!!!!!!!!! \n\nThe result is: \n" + str(result) + "\n\n!!!!!!!!!!!!!")