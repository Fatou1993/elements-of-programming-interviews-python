from collections import deque

class GraphVertex :

    def __init__(self):
        self.d = -1
        self.edges = []

def is_any_placement_possible(G):
    """
    G = list of vertices
    :param G:
    :return:
    """
    def bfs(s):
        q = deque([s])
        s.d = 0
        while q :
            v = q.popleft()
            for e in v.edges :
                if e.d == -1:
                    e.d = v.d + 1  # flipped color
                    q.append(e)
                elif e.d == v.d :
                    return False

        return True

    return all(v.d == -1 and bfs(v) for v in G )



