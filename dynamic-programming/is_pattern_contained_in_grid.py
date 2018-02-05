from sets import Set
def is_pattern_contained_in_grid_using_cache(grid, S):
    def is_pattern_contained_in_grid_helper(i, j, k):
        if k == s:
            return True
        if i <n and j < m and grid[i][j] == S[k] and (i,j,k) not in previous_attempts:
            if is_pattern_contained_in_grid_helper(i + 1, j, k + 1) | is_pattern_contained_in_grid_helper(i - 1, j,
                                                                                                              k + 1) | is_pattern_contained_in_grid_helper(
                i, j - 1, k + 1) | is_pattern_contained_in_grid_helper(i, j + 1, k + 1) :
                return True
        previous_attempts.add((i, j, k))
        return False

    n = len(grid)
    if n == 0:
        return not S
    m = len(grid[0])
    s = len(S)
    previous_attempts = Set()
    return any (is_pattern_contained_in_grid_helper(i, j, 0) for i in range(n) for j in range(m))

if __name__ == "__main__" :
    #use a set for previous attempts and when searching start at multiple points
    grid = [[1,2,3],[3,4,5],[5,6,7]]
    S = [1,3,4,6,7]
    print(is_pattern_contained_in_grid_using_cache(grid, S))