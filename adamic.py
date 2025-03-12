import igraph as ig

g = ig.Graph()

g.add_vertices(34)

with open("karate.edgelist", "r") as file:
    edges = [tuple(map(int, line.strip().split())) for line in file]

g.add_edges(edges)


for i in range(34):
    for j in range(i + 1, 34):
        degree_i = len(g.neighbors(i))
        degree_j = len(g.neighbors(j))


        preferential_attachment = degree_i * degree_j


        print(f"Preferential Attachment between nodes {i} and {j}:")
        print(f"Degree of node {i}: {degree_i}")
        print(f"Degree of node {j}: {degree_j}")
        print(f"Preferential Attachment score: {preferential_attachment}")
        print("-" * 40)


