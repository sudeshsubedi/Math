from typing import List
import numpy as np
from custom_utils import determinant

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





if __name__=="__main__":
    data = [
        [1],
        [1]
    ]
    for i in range(0):
        print("test")
    matrix = Matrix(2, 1, data)
    print(matrix.getData().shape)
