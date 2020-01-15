import sys
import random
import math
import EntityPoint
import numpy as np

def errors(j,groupJ,group,relation,size):
    count = 0
    for i in range(0,size):
        if relation[i][j] == -1 and groupJ == group[i] or relation[i][j] == 1 and groupJ != group[i]:
            count+=1
    return count

def possibleConflicts(i, groupI, group, relation, size):
    return errors(i, groupI, group, relation, size)

def conflicts(i,group, relation, size):
    return errors(i, group[i], group, relation, size)


def calculate(group,relation,size):
    conf = 0;
    for i in range(0,size):
        conf += conflicts(i, group, relation,size)

    return conf/2


# def error(j,group,relation,size):
#     count = 0
#     for i in range(0,size):
#         if relation[i][j] == -1 and group[j] == group[i] or relation[i][j] == 1 and group[j] != group[i]:
#             count+=1
#     return count


def error2(j,group,relation,size):
    count = 0
    for i in range(0,size):
        if relation[i][j] == 1 and group[j] == group[i] or relation[i][j] == -1 and group[j] != group[i]:
            count+=1
    return count


# def errors(group,relation,size):
#     e = 0
#     for i in range(0,size):
#         e+=error(i,group,relation,size)
#     return e


def errors2(group,relation,size):
    e = 0
    for i in range(0,size):
        e+=error2(i,group,relation,size)
    return e


#def conflicts(group,relation,size):
#    return errors(group,relation,size)/2


def conflicts2(group,relation,size):
    return errors2(group,relation,size)/2


def normalize(g):
    norm = np.copy(g)

    for i in range(0, len(norm)):
        norm[i] = -1

    print(norm)

    norm[g[0]] = 0
    k = 1
    for i in range(1, len(g)):
        if norm[g[i]] == -1:
            norm[g[i]] = k
            k += 1

    for i in range(0, len(g)):
        g[i] = norm[g[i]]


def main():
    print("ok")
    relation = np.zeros((5, 5))

    relation[0][1] = 1
    relation[1][0] = 1

    relation[3][2] = -1
    relation[2][3] = -1
    relation[1][2] = -1
    relation[2][1] = -1
    relation[0][2] = -1
    relation[2][0] = -1

    for i in range(0,4):
        relation[i][4]=1
        relation[4][i] = 1

    print(relation)

    group = np.zeros(5)
    print("group: ",group)

    print("2. elem miatti hibak: ",errors(2,0,group,relation,5))
    print("4. elem ha 1 elso csoportban lenne: ",possibleConflicts(4,1,group,relation,5))
    print("0. elem miatti hiba conflicts: ",conflicts(0,group,relation,5))
    print("osszes hiba: ",calculate(group,relation,5))

if __name__ == '__main__':
    main()