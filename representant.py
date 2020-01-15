import numpy as np

def initial_state(clusters):
    for c in clusters:
        for i in range(len(c)):
            for j in range(i + 1, len(c)):
                c[i].a = 0
                c[j].a = 0
                c[i].b = 0
                c[j].b = 0
                c[i].r1 = 0
                c[j].r1 = 0

def calculate_values(clusters,relation):
    for c in clusters:
        for i in range(len(c)):
            for j in range(i + 1, len(c)):
                id_i = c[i].id
                id_j = c[j].id
                if relation[id_i][id_j] == 1:
                    c[i].a += 1
                    c[j].a += 1
                if relation[id_i][id_j] == -1:
                    c[i].b += 1
                    c[j].b += 1


def calculateRvalues(clusters,w,v):
    for c in clusters:
        for i in range(len(c)):
            c[i].r1 = (c[i].a**w - c[i].b**v)/(c[i].a+c[i].b+1)

def getRepresentants(clusters,relation,w,v):

    initial_state(clusters)
    calculate_values(clusters,relation)
    calculateRvalues(clusters,w,v)

    rows, columns = relation.shape
    representants = [-1]*rows

    #clusters = np.asarray(clusters)

    for i in range(len(clusters)):
        if len(clusters[i]) == 1:
            continue

        max = -np.inf
        #np.amax + lambda?
        for j in range(len(clusters[i])):
            if clusters[i][j].r1 > max:
                max=clusters[i][j].r1
                max_element = clusters[i][j]
        representants[i]=max_element

    representants = [item for item in representants if item != -1]


    return representants



def closestRepresentant(representants,element,type):
    index = 0
    min = element.distance(representants[0],type)

    for i in range(1,len(representants)):
        if representants[i] == element:
            continue
        d = element.distance(representants[i],type)
        if d < min:
            min = d
            index = i
    return index

