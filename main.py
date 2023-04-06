import networkx as nx

# Read the adjacency matrices from two files
with open('graph1.txt', 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    G1 = nx.Graph()
    for i in range(1, n+1):
        row = [int(x) for x in lines[i].split()]
        G1.add_node(i)
        for j in range(i, n+1):
            if row[j-1] != 0:
                G1.add_edge(i, j)

with open('graph2.txt', 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    G2 = nx.Graph()
    for i in range(1, n+1):
        row = [int(x) for x in lines[i].split()]
        G2.add_node(i)
        for j in range(i, n+1):
            if row[j-1] != 0:
                G2.add_edge(i, j)

# Check if the graphs are isomorphic
if nx.is_isomorphic(G1, G2):
    print('The graphs are isomorphic')
else:
    print('The graphs are not isomorphic')
