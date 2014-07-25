def two_bit_flip(node):
    node_list = list(node)
    out = set()
    bit_length = len(node_list)
    for i in range(bit_length):
        for j in range(bit_length):
            new_node = node_list[:]
            if i != j:
                new_node[i] = ('1' if node[i] == '0' else '0')
                new_node[j] = ('1' if node[j] == '0' else '0')
            else:
                new_node[i] = ('1' if node[i] == '0' else '0')
            out.add(''.join(new_node))
    return out

def find_set(node, nodes):
    if node != nodes[node][0]:
        nodes[node][0] = find_set(nodes[node][0], nodes)
    return nodes[node][0]

def link(node1, node2, nodes):
    if nodes[node1][1] > nodes[node2][1]:
        nodes[node2][0] = node1
    else:
        nodes[node1][0] = node2
        if nodes[node1][1] == nodes[node2][1]:
            nodes[node2][1] += 1

def union(node1, node2, nodes):
    link(find_set(node1, nodes), find_set(node2, nodes), nodes)

def clustering(nodes):
    all = set(nodes.keys())
    num = len(all)
    for node1 in all:
        nearby = two_bit_flip(node1)
        actual = nearby.intersection(all)
        for node2 in actual:
            if find_set(node1, nodes) != find_set(node2, nodes):
                union(node1, node2, nodes)
                num -= 1
    return num

def main():
    nodes = {}
    infile = open('clustering_big.txt', 'r')
    infile.readline()
    lines = infile.readlines()
    for line in lines:
        bits = line.split()
        node = ''.join(bits)
        nodes[node] = [node, 0]
    print clustering(nodes)

if __name__ == '__main__':
    main()
