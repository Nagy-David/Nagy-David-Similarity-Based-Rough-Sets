"""Generate random graphs."""
import pathlib
import random
import numpy as np
from PyQt5.QtCore import QTime, QDate


class Graph(object):
    """Abstract class."""

    edges_list = []

    def sign(self, q):
        """we have signed edges."""
        p = random.random()
        if p < q:
            return 1
        else:
            return -1

    def get_edges(self):
        """A getter."""
        return self.edges_list

    def number_of_edges(self):
        """Number of edges in the graph."""
        return len(self.edges_list)

    def set_edges(self, edges):
        """A setter for testing."""
        self.edges_list = edges

    def conflicts(self, uf):
        """Calculate conflicts."""
        counter = 0
        for i, j, v in self.edges_list:
            if (uf[i] == uf[j] and v == -1) or (uf[i] != uf[j] and v == 1):
                counter += 1
        return counter

    def recolor(self, count):
        """Recolor count number of negative edges."""
        minus = [(i, j) for i, j, v in self.edges_list if v < 0]
        if len(minus) > count:
            to_change = random.sample(minus, count)
        else:
            to_change = minus
        for c, x in enumerate(self.edges_list):
            i, j, v = x
            if (i, j) in to_change:
                self.edges_list[c] = (i, j, 1)

    def q_rate(self):
        """calculate q."""
        positive = 0
        negative = 0
        for i, j, v in self.edges_list:
            if v > 0:
                positive += 1
            if v < 0:
                negative += 1
        return positive/(positive+negative)


class ERGraph(Graph):
    """Erdős-Rényi random graph."""

    def __init__(self, N, p, q):
        """Generate it."""
        self.edges_list = []
        for i in range(N-1):
            for j in range(i+1, N):
                if random.random() < p:
                    self.edges_list.append((i, j, self.sign(q)))


class BAGraph(Graph):
    """Barabási-Albert random graph."""

    def __init__(self, N, q, m0=3, m=2):
        """Generate it."""
        total_degree = 0
        degree_list = []
        self.edges_list = []

        shuffling = list(range(N))
        random.shuffle(shuffling)
        for i in range(m0):                 # core -- a complete graph
            for j in range(m0):
                if i != j:
                    si = shuffling[i]
                    sj = shuffling[j]
                    self.edges_list.append((si, sj, self.sign(q)))
                    total_degree += 1
            degree_list.append(m0)

        for current_node in range(m0, N):
            nodes_to_connected = []
            while len(nodes_to_connected) < m:
                # connect by preference
                rand = random.randint(1, total_degree)
                sum = 0
                for i in range(len(degree_list)):
                    sum += degree_list[i]
                    if rand <= sum:
                        node_to_connect = i
                        break
                if node_to_connect in nodes_to_connected:
                    continue
                else:
                    nodes_to_connected.append(node_to_connect)
                    self.edges_list.append((
                        shuffling[current_node],
                        shuffling[i],
                        self.sign(q)))
                    degree_list[node_to_connect] += 1

            degree_list.append(m)
            total_degree += m * 2


# usage:
#a = BAGraph(size,0.6)

#gráfgenerálás:
#először méret szerint majd p értéke szerint
for size in range(100,500,100):

    for p in [0.5,0.7]:

        a = ERGraph(size,p,0.5)
        relation = np.zeros((size,size),dtype=int)
        edges = a.get_edges()

        for e in edges:
            row = e[0]
            column = e[1]
            value = e[2]
            if value == -1:
                value = 2
            relation[row][column] = value
            relation[column][row] = value

        time = QTime.currentTime()
        now = QDate.currentDate()
        s = str(now.year()) + "_" + str(now.month()) + "_" + str(now.day()) + "_" + str(time.hour()) + "_" + str(
            time.minute()) + "_" + str(time.second())

        path_p = "p_"+str(p)
        path = 'Output\\Relations\\ER\\'+path_p+"\\"
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        # Qdate legyen azonosító, utána méret és p érték
        path += "er_relation_" + s + "_"+ str(size)+ "points_" + path_p +".txt"
        with open("test.txt", 'wb') as f:
            np.savetxt(path, relation, delimiter='', newline='\r\n', fmt='%d', header=str(size), comments='')

#print(a.get_edges(), a.q_rate())
#a.recolor(8)
#print(a.get_edges(), a.q_rate())
