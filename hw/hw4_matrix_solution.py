import random
class Array2D :
    # Creates a 2-D array of size numRows x numCols.
    def __init__( self, numRows, numCols ):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = [None] * numRows

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( numRows ) :
            self._theRows[i] = [None] * numCols

    # Returns the number of rows in the 2-D array.
    def numRows( self ):
        return len( self._theRows )

    # Returns the number of columns in the 2-D array.
    def numCols( self ):
         return len( self._theRows[0] )

    # Clears the array by setting every element to the given value.
    def clear( self, value ):
        for row in range( self.numRows() ):
            for col in range(self.numCols()):
                self[row, col] = value
                
    # Gets the contents of the element at position [i, j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
        and col >= 0 and col < self.numCols(), \
        "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
        and col >= 0 and col < self.numCols(), \
        "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value


class Matrix :
    #Creates a matrix of size numRows x numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._theGrid = Array2D( numRows, numCols )
        self._theGrid.clear( 0 )

    # Returns the number of rows in the matrix.
    def numRows( self ):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix.
    def numCols( self ):
        return self._theGrid.numCols()

    # Returns the value of element (i, j): x[i,j]
    def __getitem__( self, ndxTuple ):
        return self._theGrid[ ndxTuple[0], ndxTuple[1] ]

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__( self, ndxTuple, scalar ):
        self._theGrid[ ndxTuple[0], ndxTuple[1] ] = scalar

    # Returns the maximum value within this(self) matrix
    def max_value(self):
        to_return = self[0,0]
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                if self[r, c] > to_return:
                    to_return = self[r, c]
        return to_return   

    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                self[ r, c ] *= scalar

    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose( self ):
        # To do ......
        newmatrix = Matrix(self.numCols(),self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                value = self[i,j]
                newmatrix[j, i] = self[i,j]
        return newmatrix
        

    # Creates and returns a new matrix that results from matrix addition.
    def __add__( self, rhsMatrix ):
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[r,c] = self[r,c] + rhsMatrix[r,c]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__( self, rhsMatrix ):
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[r,c] = self[r,c] - rhsMatrix[r,c]
        return newMatrix

    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__( self, rhsMatrix ):
        # To do ......
        newmatrix = Matrix(self.numRows(),rhsMatrix.numCols())
        for m in range(self.numRows()):
            for i in range(rhsMatrix.numCols()):
                newmatrix[m,i] = 0
                for j in range(self.numCols()):
                    newmatrix[m,i] += self[m, j] * rhsMatrix[j, i]
        return newmatrix

    def __str__(self):
        answer = []  # Use list for efficiency
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                answer.append(str(self[row, col]) + '\t')
            answer.append('\n')
        return ''.join(answer)





