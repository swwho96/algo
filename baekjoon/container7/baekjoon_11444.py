def multiple_matrix(mat1, mat2):
    result = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k]*mat2[k][j] % 1000000007
    return result

def divide_and_conquer(a, b):
    if b == 1:
        return a
    tmp = divide_and_conquer(a, b//2)
    if b % 2 == 0:
        return multiple_matrix(tmp, tmp)
    else:
        return multiple_matrix(multiple_matrix(tmp, tmp), a)

n = int(input())
matrix = [[1,1],[1,0]]
matrix = divide_and_conquer(matrix, n)
print(matrix[0][1] % 1000000007)