class Edge:
    def __init__(self, p1, p2, cost):
        self.p1 = p1
        self.p2 = p2
        self.cost = cost

p = {}
rank = {}

def make_set(x):
    p[x] = x
    rank[x] = 0

def link(s1, s2):
    if rank[s1] > rank[s2]:
        p[s2] = s1
    else:
        p[s1] = s2
        if rank[s1] == rank[s2]:
            rank[s2] = rank[s2] + 1

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(s1, s2):
    link(find_set(s1), find_set(s2))

def partition(edges, l, r):
    pivot = edges[l]
    i = l + 1
    for j in range(l+1, r+1):
        if edges[j].cost < pivot.cost:
            edges[i], edges[j] = edges[j], edges[i]
            i += 1
    edges[l], edges[i-1] = edges[i-1], edges[l]
    return i - 1

def quicksort(edges, l, r):
    if l < r:
        q = partition(edges, l, r)
        quicksort(edges, l, q - 1)
        quicksort(edges, q + 1, r)

import sys
def clustering(edges, k):
    quicksort(edges, 0, len(edges) - 1)
    cluster_num = len(p.keys())
    for edge in edges:
        if cluster_num == k:
            break
        if find_set(edge.p1) != find_set(edge.p2):
            union(edge.p1, edge.p2)
            cluster_num -= 1
    
    distance = sys.maxint
    for edge in edges:
        if find_set(edge.p1) != find_set(edge.p2) and edge.cost < distance:
            distance = edge.cost

    print distance

def main():
    infile = open('clustering1.txt', 'r')
    infile.readline()
    lines = infile.readlines()
    edges = []
    for line in lines:
        p1, p2, cost = line.split()
        edges.append(Edge(p1, p2, int(cost)))
        if p1 not in p and p1 not in rank:
            make_set(p1)
        if p2 not in p and p2 not in rank:
            make_set(p2)
    clustering(edges, 4)

if __name__ == '__main__':
    main()
