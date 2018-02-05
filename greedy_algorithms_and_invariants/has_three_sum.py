def has_three_summ(A,t):
    A.sort()
    n = len(A)
    for k in range(n):
        target = t - A[k]
        i, j = 0, n-1
        while i < j :
            if A[i]+A[j] == target :
                return (A[i], A[j], A[k])
            elif A[i]+A[j] < target :
                i+=1
            else:
                j-=1
    return None

if __name__ == "__main__":
    A = [11,2,5,7,3]
    print(has_three_summ(A,22))
