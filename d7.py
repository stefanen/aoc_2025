day = '7'
input = open('./input_d_' + day + '.txt').read()
lines=[e for e in input.split('\n')]
col_length=len(lines)-1
row_length=max([len(lines[c]) for c in range(0,col_length)])
matrix=[[list(lines[y])[x] for x in range(0,row_length)] for y in range(0,col_length)]

def memoize(fn):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result
    return wrapper


def get_start_indices(matrix):
    for y in range(0,col_length):
        for x in range(0,row_length):
            if matrix[y][x]=='S':
                return (y,x)

@memoize
def sol(y,x):
    if y>col_length-2:
        return 1
    if matrix[y+1][x]=='.':
        return sol(y+1,x)
    if matrix[y+1][x]=='^':
        return sol(y+1,x+1)+sol(y+1,x-1)

print(sol(*get_start_indices(matrix)))



