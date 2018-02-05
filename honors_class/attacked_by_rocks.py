def attacked_by_rocks(square):
    n = len(square)
    for row in range(n):
        for col in range(n):
            if square[row][col] == 0 :
                dfs(square, n, row, col)

    for row in range(n):
        for col in range(n):
            if square[row][col] == -1 :
                square[row][col] = 0

def dfs(square, n, row, col) :
    if not (0<=row<n) or not(0<=col<n) or square[row][col] == - 1 :
        return
    square[row][col] = - 1
    dfs(square, n, row+1, col)
    dfs(square, n, row-1, col)
    dfs(square, n, row, col+1)
    dfs(square, n, row, col-1)
    return

if __name__ == "__main__":
    square = [
        [1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]
    attacked_by_rocks(square)
    print square