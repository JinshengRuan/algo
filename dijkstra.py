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
        self.size = self.size - 1
        self.min_heapify(0, d)
        return min

    def update(self, v, d):
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

def testMinHeap():
    d = {'A':0, 'B':1000000, 'C':1000000, 'D':1000000, 'E':1000000}
    minheap = MinHeap(d)
    print minheap
    d['B'] = 10
    d['C'] = 3
    minheap.update('B', d)
    minheap.update('C', d)
    print minheap
    d['B'] = 7
    d['D'] = 11
    d['E'] = 2
    minheap.update('B', d)
    minheap.update('D', d)
    minheap.update('E', d)
    print minheap
    d['D'] = 9
    minheap.update('D', d)
    print minheap
    u = minheap.extract_min(d)
    print u
    print minheap

def dijkstra(G, w, s):
    dis = {}
    path = {}
    for v in G.adj.keys():
        dis[v] = 99999999
        path[v] = None
    dis[s] = 0

    S = set([])
    Q = MinHeap(dis)
    while Q.size > 0:
        u = Q.extract_min(dis)
        S.add(u)
        for v in G.adj[u]:
            if dis[v] > dis[u] + w[(u,v)]:
                dis[v] = dis[u] + w[(u,v)]
                Q.update(v, dis)
                path[v] = u
    print dis['7'],dis['37'],dis['59'],dis['82'],dis['99'],dis['115'],dis['133'],dis['165'],dis['188'],dis['197']

def main():
    w = {}
    g = Graph()
    infile = open('dijkstraData.txt', 'r')
    lines = infile.readlines()
    for line in lines:
        vertices = line.split()
        for i in range(1, len(vertices)):
            vertex, weight = vertices[i].split(',')
            g.add_edge(vertices[0], vertex)
            w[(vertices[0], vertex)] = int(weight)
    dijkstra(g, w, '1')

if __name__ == '__main__':
#    testMinHeap()
    main()
