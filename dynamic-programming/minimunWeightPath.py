def minimumTotal(triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if not n : return 0
        dp = [triangle[0][0]]
        length = 1
        for i in range(1,n):
            tmp = []
            for j in range(i+1):
                if j <= i - 1 and j < 1:
                    tmp.append(triangle[i][j] + dp[j])
                elif j > i - 1 and j >= 1 :
                    tmp.append(triangle[i][j] + dp[j-1])
                else:
                    tmp.append(triangle[i][j] + min(dp[j-1], dp[j]))
            dp = tmp
        return min(dp)

if __name__ == "__main__":
    triangle = [[2],[3,4], [6,5,7], [4,1,8,3]]
    print(minimumTotal(triangle))