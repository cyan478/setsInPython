def union(A, B):
    return [x for x in A if x not in B] + intersect(A,B) + [x for x in B if x not in A]
def intersect(A, B):
    return [x for x in A if x in B]
def setDiff(A, B):
    return [x for x in A if x not in B]
def symDiff(A, B):
    return union(setDiff(A,B), setDiff(B,A))
def cartProd(A, B):
    return [[a,b] for a in A for b in B]

