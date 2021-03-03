from DataStructure.Matrix import Matrix
def main():
    pass

if __name__=="__main__":
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = Matrix(3, 3, data)

    data = [
        [1, 2, 3, 4, 5],
        [3, 6, 8, 9, 2],
        [1, 9, 4, 3, 5]
    ]
    matrix2 = Matrix(3, 5, data)
    print(matrix*matrix2)