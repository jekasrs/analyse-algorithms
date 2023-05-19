# Числа Фибоначчи:
# f[0] = 0
# f[1] = 1
# f[i + 2] = f[i+1] + f[i] = 1, где  i = 0
# f[i + 2] = f[i+1] + f[i] = 2, где  i = 1
# ...
# f[n] = f[n-1] + f[n-2]

# Индуктивное равенство
#        n
# ( 1 1 ) = (f[n+1] f[n]   )
# ( 1 0 ) = (f[n]   f[n-1] )
#

def getFibonacci(n):
    matrix = [[1, 1],
              [1, 0]]
    i_matrix = matrix
    if n == 0:
        return 0
    for i in range(1, n):
        a00 = i_matrix[0][0] * matrix[0][0] + i_matrix[0][1] * matrix[1][0]
        a01 = i_matrix[0][0] * matrix[1][0] + i_matrix[0][1] * matrix[1][1]
        a10 = i_matrix[1][0] * matrix[0][0] + i_matrix[1][1] * matrix[1][0]
        a11 = i_matrix[1][0] * matrix[1][0] + i_matrix[1][1] * matrix[1][1]

        i_matrix = [[a00, a01], [a10, a11]]

    return i_matrix[0][1]


if __name__ == '__main__':
    print(f'0 : {getFibonacci(0)}')
    print(f'1 : {getFibonacci(1)}')
    print(f'2 : {getFibonacci(2)}')
    print(f'3 : {getFibonacci(3)}')
    print(f'4 : {getFibonacci(4)}')
    print(f'5 : {getFibonacci(5)}')
    print(f'6 : {getFibonacci(6)}')
    print(f'7 : {getFibonacci(7)}')
    print(f'8 : {getFibonacci(8)}')

