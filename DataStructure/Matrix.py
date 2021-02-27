from typing import List
import numpy as np
from custom_utils import determinant, generateIdentityMatrixData

class Matrix:
    def __init__(self, rows:int, cols:int, data:list[list[int]]):
        if(type(data) != list or type(data[0]) !=list):
            raise Exception("Data should be 2d list matching the order of matrix provided")
        if rows!=len(data) and cols!=len(data[0]):
            raise Exception("The order of matrix did not match the data provided")
        elif not (rows>0 and cols>0):
            raise Exception("No of rows and columns of matrix cannot be zero or negative")
        for col in data:
            if(len(col) != cols):
                raise Exception("Each row of matrix should contain same no of element")
        self.__data = np.array(data, np.float64)
        self.i = rows
        self.j = cols
        self.isSquare = rows == cols

    def getData(self):
        return self.__data

    def determinant(self):
        if not self.isSquare:
            return "Non square matrix don't have determinant"
        
        if self.i == 1:
            return self.__data[0][0]
        
        return determinant(self.__data)

    def __gauss_jordan(self):
        if not self.isSquare:
            raise Exception("Cannot find the inverse of non square matrix")
        if self.determinant() == 0:
            raise Exception("Cannot find the inverse of singular matrix")

        identityEquivalent = np.array(generateIdentityMatrixData(self.i), dtype=np.float64)
        dataEquivalent = self.__data
        for col in range(self.i):
            if dataEquivalent[col][col] != 1:
                tempDivisionFactor = dataEquivalent[col][col]
                dataEquivalent[col] = dataEquivalent[col]/tempDivisionFactor
                identityEquivalent[col] = identityEquivalent[col]/tempDivisionFactor
            for i in range(self.i):
                if i==col:
                    continue
                tempSubFactor = dataEquivalent[i][col]
                dataEquivalent[i] = dataEquivalent[i] - dataEquivalent[col] * tempSubFactor
                identityEquivalent[i] = identityEquivalent[i] - identityEquivalent[col] * tempSubFactor
        return identityEquivalent
    def inverse(self):
        return Matrix(self.i, self.i, np.ndarray.tolist(self.__gauss_jordan()))




if __name__=="__main__":
    data = [
        [2, -1, 4],
        [1, 0, -4],
        [6, -1, 2]
    ]
    matrix = Matrix(3, 3, data)

    print(matrix.inverse().getData())
