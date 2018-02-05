from collections import defaultdict

def find_largest_number_teams(teams):
    n, m = len(teams), len(teams[0])
    for i in range(n):
        teams[i].sort()

    #create graph
    graph = defaultdict(set)
    for i in range(n):
        for j in range(i+1,n):
            if all(teams[i][k] > teams[j][k] for k in range(m-1,-1,-1)) :
                #teams[i] can be placed back team[j]
                graph[i].add(j)
            elif all(teams[j][k] > teams[i][k] for k in range(m-1,-1,-1)) :
                graph[j].add(i)

    #determine longest path in graph
    dist = [[float('-inf') if i!= j else 0 for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if v in graph[u]:
                dist[u][v] = 1

    for u in range(n):
        for v in range(n):
            for c in graph[u]:
                dist[u][v] = max(dist[u][v], dist[u][c] + dist[c][v])
    return max(dist)

if __name__ == "__main__":
    teams = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print(find_largest_number_teams(teams))



