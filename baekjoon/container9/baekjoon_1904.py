# dp를 활용한 풀이 -> O(N)

N = int(input())
if N == 1:
    print(1)
else:
    a, b = 1, 2
    for _ in range(N-2):
        a, b = b, (a + b) % 15746
    print(b)

# 행렬을 활용한 풀이 -> O(logN)

def matrix_multiply(A:list, B:list)->list:
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0])%15746, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%15746],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%15746, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%15746]
    ]

def matrix_power(A:list, n:int)->list:
    if n == 1:
        return A
    if n % 2 == 0:
        tmp_list = matrix_power(A, n//2)
        return matrix_multiply(tmp_list, tmp_list)
    else:
        return matrix_multiply(A, matrix_power(A, n-1))
    
def cnt_bi_nums(n:int)->int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    A = [[1,1], [1,0]]
    result = matrix_power(A, n-1)
    return (result[0][0] + result[0][1])%15746

N = int(input())
print(cnt_bi_nums(N))