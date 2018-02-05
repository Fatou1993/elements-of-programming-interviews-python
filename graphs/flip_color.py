def flip_color(x,y,A):
    def dfs(x,y, initial_color):
        if x >= n or x < 0 or y >= m or y < 0 or A[x][y]  != initial_color :
            return

        A[x][y] = 1 - initial_color

        dfs(x-1,y, initial_color)
        dfs(x+1, y, initial_color)
        dfs(x, y-1, initial_color)
        dfs(x, y+1, initial_color)

    n, m = len(A), len(A[0])
    initial_color = A[x][y]
    dfs(x,y, initial_color)
    return A

if __name__ == "__main__":
    A = [[1,0,1,0,0,0,1,1,1,1], [0,0,1,0,0,1,0,0,1,1], [1,1,1,0,0,1,1,0,1,1], [0,1,0,1,1,1,1,0,1,0], [1,0,1,0,0,0,0,1,0,0],
         [1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [0,0,0,0,1,0,1,0,0,1], [1,0,1,0,1,0,1,0,0,0], [1,0,1,1,0,0,0,1,1,1], [0,0,0,0,0,0,0,1,1,0]]
    x,y = 5, 4
    for i in range(10):
        print(A[i])
    print('')
    result = flip_color(x,y,A)
    for i in range(10):
        print(result[i])
    print('')
    x, y = 3, 6
    result1 = flip_color(x, y, result)
    for i in range(10):
        print(result1[i])
