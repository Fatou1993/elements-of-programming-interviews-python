class GraphVertex :
    white, grey, black = range(3)

    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []

def is_deadlock(G):
    def has_cycle(cur):
        if cur.color == GraphVertex.grey : #visiting a grey vertex means a cyce
            return True
        cur.color = GraphVertex.grey #start visit
        if any(v.color != GraphVertex.black and has_cycle(v) for v in cur.edges):
            return True
        cur.color = GraphVertex.black #end visit
        return False
    return any(vertex.color == GraphVertex.white and has_cycle(vertex) for vertex in G)