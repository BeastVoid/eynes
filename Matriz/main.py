import random
import doctest


COLUMNS = 5
ROWS = 5

def connect_four(matrix):
    """ 
    Check connect four match 

    Vertical match

    >>> connect_four([ [3, 4, 4, 4, 6], [5, 4, 6, 7, 8], [5, 4, 5, 3, 3], [5, 6, 5, 3, 3], [5, 0, 5, 1, 2] ])
    {'Connect four': True, 'First match': [1, 0], 'Ending match': [4, 0]}

    Horizontal match

    >>> connect_four([ [3, 4, 4, 4, 4], [5, 4, 6, 7, 8], [5, 4, 5, 3, 3], [3, 6, 5, 3, 3], [5, 0, 5, 1, 2] ])
    {'Connect four': True, 'First match': [0, 1], 'Ending match': [0, 4]}

    No match

    >>> connect_four([ [3, 4, 4, 4, 1], [5, 4, 6, 7, 8], [5, 4, 5, 3, 3], [3, 6, 5, 3, 3], [5, 0, 5, 1, 2] ])
    {'Connect four': False, 'First match': None, 'Ending match': None}
    """

    # Horizontal
    for column in range(COLUMNS - 3):
        for row in range(ROWS):
            if matrix[row][column] == matrix[row][column + 1] == matrix[row][column + 2] == matrix[row][column + 3]:
                return {
                    'Connect four': True,
                    'First match': [row, column],
                    'Ending match': [row, column + 3]
                }
    # Vertical
    for column in range(COLUMNS):
        for row in range(ROWS - 3):
            if matrix[row][column] == matrix[row + 1][column] == matrix[row + 2][column] == matrix[row + 3][column]:
                return {
                    'Connect four': True,
                    'First match': [row, column],
                    'Ending match': [row + 3, column]
                }  
    
    return {
        'Connect four': False,
        'First match': None,
        'Ending match': None
    }  

def create_matrix():
    """
    Creates a matrix of random integers.

    >>> len(create_matrix())
    5

    """
    random.seed()
    matrix = []
    for i in range(ROWS):
        matrix.append([])
        for j in range(COLUMNS):
            matrix[i].append(random.randint(1, 100))
    
    return matrix

if __name__ == "__main__":
    doctest.testmod()
