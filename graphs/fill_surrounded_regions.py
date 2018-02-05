def fill_surrounded_regions(board):
    def canReachBoard(i,j):
        if i >= n or i < 0 or j>= m or j < 0 or visited[i][j] or board[i][j] == 1 :
            return False
        visited[i][j] = True
        if i == n-1 or i == 0 or j == m-1 or j == 0 : #reached board
            return True
        board[i][j] = 1
        if canReachBoard(i+1,j) or canReachBoard(i-1,j) or canReachBoard(i,j-1) or canReachBoard(i,j+1):
            board[i][j] = 0 #backtrack
            return True
        return False

    n, m = len(board), len(board[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 0:
                res = canReachBoard(i,j)
    return board

if __name__ == "__main__":
    board = [[1,1,1,1],[0,1,0,1],[1,0,0,1],[1,1,1,1]]
    result = fill_surrounded_regions(board)
    for i in range(4):
        print result[i]

