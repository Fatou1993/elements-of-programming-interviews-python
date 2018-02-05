def hasPath(maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """

    def hasPathHelper(cur):
        if cur[0] >= n or cur[0] < 0 or cur[1] >= m or cur[1] < 0 or maze[cur[0]][cur[1]] == 1:
            return False
        maze[cur[0]][cur[1]] = 1  # mark as visited
        if cur[0] == destination[0] and cur[1] == destination[1]:
            return True
        if hasPathHelper([cur[0] - 1, cur[1]]) or hasPathHelper([cur[0], cur[1] - 1]) or hasPathHelper(
                [cur[0] + 1, cur[1]]) or hasPathHelper([cur[0], cur[1] + 1]):
            return True
        return False

    n, m = len(maze), len(maze[0])
    return hasPathHelper(start)

