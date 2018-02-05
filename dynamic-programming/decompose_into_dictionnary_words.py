from sets import Set
def decompose_into_dictionnary_words(domain, dictionary):
    n = len(domain)
    dp = [False]*(n+1) #dp[i] = True if domain[:i] can be decomposed
    dp[0] = True
    for i in range(1,n+1):
        #dp[i] = domain[:i] in dictionary
        j = 0
        while j < i and not dp[i]:
            dp[i] = (domain[j:i] in dictionary) and dp[j]
            j+=1
    return dp[n]

if __name__ == "__main__":
    domain = "amanaplanacanal"
    dictionnary = Set(["canal", "bath", "man", "plan", "hand", "a"])
    print(decompose_into_dictionnary_words(domain, dictionnary))