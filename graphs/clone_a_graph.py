class GraphVertex :
    def __init__(self, label):
        self.label = label
        self.edges = []

    def __str__(self):
        res = str(self.label)
        for v in self.edges :
            res += " " + str(v)
        return res

def clone_graph(G):
    if not G :
        return G
    new_G = [GraphVertex(g.label) for g in G] #add labels
    mapping = {}
    for i, g in enumerate(G) :
        mapping[g] = new_G[i]
    #add references
    for g in G :
        for v in g.edges :
            mapping[g].edges.append(mapping[v])
    return new_G


from collections import deque


def cloneGraph(self, node):
    if not node:
        return None
    q = deque([node])
    vertex_map = {node: GraphVertex(node.label)}
    while q:
        v = q.popleft()
        for e in v.edges:
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[node]


if __name__ == "__main__":
    g1 = GraphVertex(1)
    g2 = GraphVertex(2)
    g3 = GraphVertex(3)
    g4 = GraphVertex(4)
    g1.edges.append(g2)
    g2.edges.append(g3)
    g3.edges.append(g4)
    G = [g1, g2, g3, g4]
    for g in G :
        print g
    print("")
    new_G = clone_graph(G)
    for g in new_G :
        print g


