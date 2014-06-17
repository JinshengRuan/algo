class Graph:
    def __init__(self):
        self.adj = {}
    
    def addEdge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)

def reverse(G):
    GRev = Graph()
    for key in G.adj.keys():
        for vertex in G.adj[key]:
            GRev.addEdge(vertex,key)
    return GRev

def dfs(G, vertex, explored, leader):
    global t
    global f
    global s
    explored.add(vertex)
    leader[vertex] = s
    for v in G.adj[vertex]:
        if v not in explored:
            dfs(G, v, explored, leader)
    t = t+1
    f[vertex] = t

def dfsLoop(G):
    global t
    global f
    global s
    t = 0
    s = None
    explored = set()
    leader = {}
    if not f:
        print 'in first dfsLoop'
        vertices = G.adj.keys()
    else:
        print 'in second dfsLoop'
        sortedV = sorted([(v,k) for k, v in f.items()])
        vertices = [v[1] for v in sortedV]
#        print [(vertices[i],f[vertices[i]]) for i in range(len(vertices))] 
    for vertex in vertices[::-1]:
        if vertex not in explored:
            s = vertex
            dfs(G, vertex, explored, leader)
    return leader

def scc(G):
    global f
    f = {}
    Gres = reverse(G)
    print 'reverse G complete'
    leader = dfsLoop(Gres)
    print 'first dfs complete'
    leader = dfsLoop(G)
    print 'second dfs complete'
    stat = {}
    for v in leader.values():
        if v not in stat:
            stat[v] = 1
        else:
            stat[v] += 1
    n = sorted(stat.values(), reverse = True)
    print n[0:5]
 
def test():
    g = Graph()
    g.addEdge('1','4')
    g.addEdge('4','7')
    g.addEdge('7','1')
    g.addEdge('9','7')
    g.addEdge('9','3')
    g.addEdge('8','6')
    g.addEdge('6','9')
    g.addEdge('3','6')
    g.addEdge('8','5')
    g.addEdge('5','2')
    g.addEdge('2','8')
    g.addEdge('10','9')
    g.addEdge('10','6')
    g.addEdge('10','3')
    gres = reverse(g)
#    testdfs(gres)
    scc(g)


def main():
    g = Graph()
    infile = open('SCC.txt', 'r')
    lines = infile.readlines()
    for line in lines:
        points = line.split()
        g.addEdge(points[0], points[1])
    print 'construct graph complete'
    scc(g)

import sys
import threading

if __name__ == '__main__':
#    test()
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
