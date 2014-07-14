class MinHeap:
    def __init__(self, d):
        self.A = d.keys()
        self.size = len(d)
        self.build_min_heap(d)

    def min_heapify(self, i, d):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.size and d[self.A[l]] < d[self.A[i]]:
            smallest = l
        else:
            smallest = i
        if r < self.size and d[self.A[r]] < d[self.A[smallest]]:
            smallest = r
        if i != smallest:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.min_heapify(smallest, d)

    def build_min_heap(self, d):
        for i in range(self.size / 2, -1, -1):
            self.min_heapify(i, d)

    def extract_min(self, d):
        if self.size < 1:
            return None
        min = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.A.pop(self.size - 1)
        self.size = self.size - 1
        self.min_heapify(0, d)
        return min

    def update(self, v, d):
        i = 0
        for i in range(self.size):
            if self.A[i] == v:
                break
        parent = (i - 1) // 2
        while i > 0 and d[self.A[parent]] > d[self.A[i]]:
            self.A[i], self.A[parent] = self.A[parent], self.A[i]
            i = parent
            parent = (i - 1) // 2

    def __str__(self):
        return self.A[0:self.size].__str__()

class Graph:
    def __init__(self):
        self.adj = {}
    
    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)

import random

def prim(G, w, r):
    A = []
    key = {}
    edge = {}
    for v in G.adj.keys():
        key[v] = 9999999999
        edge[v] = None

    key[r] = 0
    Q = MinHeap(key)
    while Q.size != 0:
        u = Q.extract_min(key)
        for v in G.adj[u]:
            if v in Q.A and w[(u,v)] < key[v]:
                edge[v] = u
                key[v] = w[(u,v)]
                Q.update(v, key)
    sum_weight = 0
    for v in G.adj.keys():
        if v != r:
            A.append((v, edge[v]))
    for e in A:
        sum_weight += w[e]

    return sum_weight

def main():
    g = Graph()
    w = {}
    infile = open('edges.txt', 'r')
    infile.readline()
    lines = infile.readlines()
    for line in lines:
        u, v, weight = line.split()
        g.add_edge(u, v)
        w[(u,v)] = int(weight)
        w[(v,u)] = int(weight)

    start = random.choice(g.adj.keys())
    print prim(g, w, start)

def test():
    g = Graph()
    w = {}
    infile = open('testedges.txt', 'r')
    infile.readline()
    lines = infile.readlines()
    for line in lines:
        u, v, weight = line.split()
        g.add_edge(u, v)
        w[(u,v)] = int(weight)
        w[(v,u)] = int(weight)

    start = g.adj.keys()[0]
    print prim(g, w, start)

if __name__ == '__main__':
#    test()
    main()
