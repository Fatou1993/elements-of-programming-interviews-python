from collections import namedtuple
def optimimum_object_subject_to_capacity(items, capacity):
    def optimimum_object_subject_to_capacity_helper(index, val, left_capacity, path):
        if index >= n :
            return
        if left_capacity <= 0 : #no more place
            if val > results[0] :
                results[1] = list(path)
                results[0] = val 
            return
        if items[index].weight <= left_capacity :
            path.append(items[index])
            optimimum_object_subject_to_capacity_helper(index+1,val+items[index].value, left_capacity-items[index].weight, path)
            path.pop()
        optimimum_object_subject_to_capacity_helper(index+1,val, left_capacity, path)
            
    n = len(items)
    results = [0, []]
    optimimum_object_subject_to_capacity_helper(0, 0, capacity, [])
    return results

def knapsack_value(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    taken = [[False for _ in range(capacity+1)] for _ in range(n)]
    path = [False]*(n)
    for j in range(capacity+1):
        dp[0][j] = 0
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            without_using_item = dp[i-1][j]
            using_item = 0 if j < items[i-1].weight else dp[i-1][j-items[i-1].weight] + items[i-1].value
            if using_item < without_using_item :
                dp[i][j] =  without_using_item
            else:
                dp[i][j] = using_item
                taken[i-1][j] = True
            if j >= items[i-1].weight :
                dp[i][j] = max(dp[i][j], dp[i-1][j-items[i-1].weight] + items[i-1].value) #include the item[i-1]
    #Reconstruct path
    total_weight = capacity
    for i in range(n-1,-1,-1):
        if taken[i][total_weight] :
            path[i] = True
            total_weight -= items[i].weight

    print([items[i] for i in range(n) if path[i]])
    return dp[n][capacity]

if __name__ == "__main__":
    Clock = namedtuple('Clock', ("value", "weight"))
    items = [Clock(65,20), Clock(35,8), Clock(245,60), Clock(195,55), Clock(65,40), Clock(150,70), Clock(275,85), Clock(155,25),
             Clock(120,30), Clock(320, 65), Clock(75,75), Clock(40,10), Clock(200,95), Clock(100,50), Clock(220,40), Clock(99,10)]
    capacity = 130
    res = optimimum_object_subject_to_capacity(items, capacity)
    val = knapsack_value(items, capacity)
    print(res)
    print(val)
    