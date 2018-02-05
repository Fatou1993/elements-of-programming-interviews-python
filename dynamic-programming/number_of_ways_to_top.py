def number_of_ways_to_top(top, maximum_step):
    if top == 0 :
        return 1
    dp = [0]*(top+1) #dp[i] = number off ways to climb up i stairs
    dp[0] = 1
    for i in range(1,top+1):
        j = 1
        while j <= i and j <= maximum_step :
            dp[i]+=dp[i-j]
            j+=1
    return dp[top]

if  __name__ == "__main__":
    n, k = 4, 2
    print(number_of_ways_to_top(n,k))