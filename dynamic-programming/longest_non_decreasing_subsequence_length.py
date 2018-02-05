def longest_non_decreasing_subsequence_length(nums):
    if not nums: return 0
    n = len(nums)
    dp = [1] * n
    res = 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res

if __name__ == "__main__":
    A = [0,8,4,12,2,10,6,14,1,9]
    print(longest_non_decreasing_subsequence_length(A))