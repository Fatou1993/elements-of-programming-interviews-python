def maximum_revenue(coins):
    def maximum_revenue_helper(start, end):
        if start > end :
            return 0
        if dp[start][end] != - 1 :
            return dp[start][end]
        option1 =  maximum_revenue_helper(start+2, end)
        option2 = maximum_revenue_helper(start+1, end-1)
        option3 = maximum_revenue_helper(start, end-2)
        option4 = maximum_revenue_helper(start+1, end-1)
        possibility1 = coins[start] + min(option1, option2)
        possibility2 = coins[end] + min(option3, option4) #because player2 will take the optimal coins
        dp[start][end] = max(possibility1, possibility2)
        return dp[start][end]

    n = len(coins)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    res = maximum_revenue_helper(0, n-1)
    return max(res,0)

if __name__ == "__main__":
    coins = [25,5,10,5,10,5]
    print(maximum_revenue(coins))

    arr1 = [8, 15, 3, 7]
    print(maximum_revenue(arr1))

    arr2 = [2, 2, 2, 2]
    print(maximum_revenue(arr2))

    arr3 = [20, 30, 2, 2, 2, 10]
    print(maximum_revenue(arr3))
    
    arr4 = [10,25,5,1,10,5]
    print(maximum_revenue(arr4))

