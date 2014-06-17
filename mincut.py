class Graph(object):
    def __init__(self, fileName = ''):
        self.vertices = []
        self.edges = {}
        infile = open(fileName, 'r')
        for line in infile:
            words = line.split()
            self.vertices.append(words[0])
            self.edges[words[0]] = []
            for i in range(1, len(words)):
                self.edges[words[0]].append(words[i])

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

import random

def mincut(G):
    while (len(G.vertices) > 2):
        vertex1 = random.choice(G.vertices)
        vertex2 = random.choice(G.edges[vertex1])
        G.edges[vertex1].extend(G.edges[vertex2])
        for x in G.edges[vertex2]:
            lst = G.edges[x]
            for i in range(0, len(lst)):
                if lst[i] == vertex2:
                    lst[i] = vertex1
        while vertex1 in G.edges[vertex1]:
            G.edges[vertex1].remove(vertex1)
        G.vertices.remove(vertex2)
        del G.edges[vertex2]
            
    return len(G.edges[G.vertices[0]])

import copy

def main():
    g = Graph('kargerMinCut.txt')
    ##print g
    min = 10000
    for i in range(0, 100):
        cut = mincut(copy.deepcopy(g))
        if cut < min:
            min = cut
    print min

if __name__ == '__main__':
    main()
