import math

def compute_binomial_coefficient(n,k):
    if k > n :
        return 0
    previous_values, currLen = [1], 1
    for i in range(1,n+1):
        res = [0]*(i+1)
        for j in range(i+1):
            if j < currLen :
                res[j] += previous_values[j]
            if j-1>=0 :
                res[j]  += previous_values[j-1]
        previous_values, currLen = res, i+1
    #print(previous_values)
    return previous_values[k]

if __name__ == "__main__":
    n = 5
    k = 2
    #ref = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    #print(compute_binomial_coefficient(n,k), ref)
    for n in range(500):
        for k in range(n//2+1):
            ref = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
            assert compute_binomial_coefficient(n,k) == ref
        if n % 100 == 0 :
            print(n)