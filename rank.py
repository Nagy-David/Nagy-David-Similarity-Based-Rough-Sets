import numpy as np

"""
A conflict is when two objects are similar but they are in different clusters
or they are dissimilar but they are in the same cluster.
"""
def conflict(relation,partition,i,j):
    return relation[i][j]==1 and partition[i]!=partition[j] or relation[i][j]==-1 and partition[i]==partition[j]

"""
An agreement is when two objects are similar and they are in the same cluster
or they are dissimilar and they are in different clusters.
"""
def agreement(relation,partition,i,j):
    return relation[i][j]==1 and partition[i]==partition[j] or relation[i][j]==-1 and partition[i]!=partition[j]

"""
Converts a tolerance relation into a support matrix
"""
def convert_relation(relation,partition):
    rows, columns = relation.shape
    A = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            if conflict(relation,partition,i,j):
                A[i][j]=-1
            if agreement(relation,partition,i,j):
                A[i][j]=1
    return A

def powers(A, eps=1e-8):
    D = A                           # save the matrix
    R = np.ones((len(A),))          # R = 1
    D2 = D@D                        # matrix "squared"
    n = np.linalg.norm(D2@R,np.inf)
    D2 /= n  # normalized square
    steps = 1
    while np.linalg.norm(D@R-D2@R) > eps:
        D, D2 = D2, D2@D2           # swap the values
        D2 /= np.linalg.norm(D2@R,np.inf)          #normalized power
        steps += 1
    return D2, steps

"""
Computes the rank for each object
"""
def rank(relation,partition):
    A = convert_relation(relation,partition)
    B,s = powers(A)             # ranking
    E = np.ones((len(A),))      # unit vector
    R = A@(B@E)                 # ranks
    R /= max(abs(R))
    return R

"""
Assigns a rank value to each point.
"""
def assignRank(points,relation,partition):
    R = rank(relation,partition)
    for i in range(len(points)):
        points[i].rank = R[i]

"""
Returns the representatives for each cluster
"""
def getRepresentatives(clusters):
    representatives = [] #list of representatives
    for i in range(len(clusters)):
        #for each cluster the object with the maximum rank will be its representative
        max = -np.inf
        for j in range(len(clusters[i])):
            if clusters[i][j].rank > max:
                max=clusters[i][j].rank
                max_element = clusters[i][j]
        representatives.append(max_element)

    return representatives


# def closestRepresentative(representatives,element,type):
#     index = 0
#     min = element.distance(representatives[0],type)
#
#     for i in range(1,len(representatives)):
#         if representatives[i] == element:
#             continue
#         d = element.distance(representatives[i],type)
#         if d < min:
#             min = d
#             index = i
#     return index
