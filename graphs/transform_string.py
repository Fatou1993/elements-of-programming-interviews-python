from collections import defaultdict, Counter, deque
from sets import Set

def transform_string(D, s, t) :
    def differByOneCharacter(w1, w2):
        n, m = len(w1), len(w2)
        if n != m : return False
        c1 = Counter(w1)
        c2 = Counter(w2)
        return len(c1&c2) == n-1

    def create_graph(D):
        graph = defaultdict(set)
        n = len(D)
        if not n : return graph
        for i in range(n):
            for j in range(i+1,n):
                if differByOneCharacter(D[i], D[j]):
                    graph[D[i]].add(D[j])
                    graph[D[j]].add(D[i])
        return graph

    def canReach(src, dest):
        #only not visited enter this function
        visited.add(src)
        path.append(src)
        if src == dest :
            return True
        for e in graph[src]:
            if e not in visited and canReach(e, dest):
                return True
        path.pop()
        return False

    graph = create_graph(D)
    path = []
    visited = Set()
    res = canReach(s,t)
    return path

if __name__ == "__main__":
    D = ["bat","cot","cat","dog","dag","dot","cat"]
    s, t = "cat", "dog"
    print(transform_string(D,s,t))


