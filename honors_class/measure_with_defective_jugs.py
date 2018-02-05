from collections import namedtuple

Jug = namedtuple("Jug", ("low", "high"))
VolumeRange = namedtuple("VolumeRange", ("low", "high"))

def check_feasible(jugs, L, H, c=set()):
    if L > H or VolumeRange(L,H) in c or L < 0 and H < 0 :
        return False
    if any((j.low <= L and j.high <= H) or (check_feasible(jugs, L-j.low, H-j.high)) for j in jugs):
        return True
    c.add(VolumeRange(L,H))
    return False

if __name__ == "__main__":
    jugs = [Jug(230,240), Jug(290,310), Jug(500,515)]
    L, H = 2100, 2300
    print check_feasible(jugs, L, H)