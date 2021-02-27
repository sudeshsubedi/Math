import numpy as np

def determinant(data):
    if len(data) == 2:
        return data[0][0]*data[1][1] - data[0][1]*data[1][0]
    
    det = 0
    for i in range(len(data)):
        new_cols = list([x for x in range(len(data))])
        new_cols.remove(i)
        det += ((-1)**i) * determinant(data[1:, new_cols]) * data[0][i]
    return det

def generateIdentityMatrixData(n:int):
    data = []
    for i in range(n):
        rowData = [1 if i==x else 0 for x in range(n)]
        data.append(rowData)
    return data


if __name__=="__main__":
    # data = np.array([
    #     [1, 0, 0, 0, 0, 2],
    #     [0, 1, 0, 0, 2, 0],
    #     [0, 0, 1, 2, 0, 0],
    #     [0, 0, 2, 1, 0, 0],
    #     [0, 2, 0, 0, 1, 0],
    #     [2, 0, 0, 0, 0, 1]
    # ],
    # dtype=np.float64)
    # #data = np.array([[6, 1], [4, -2]], dtype=np.float64)
    # print(determinant(data))

    print(np.matrix(generateIdentityMatrixData(8)))