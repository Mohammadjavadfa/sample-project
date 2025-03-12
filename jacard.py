import igraph as ig
g = ig.Graph()

g.add_vertices(34)

with open("karate.edgelist", "r") as file:
    edges = [tuple(map(int, line.strip().split())) for line in file]

g.add_edges(edges)

for i in range(34):
    for j in range(i + 1, 34):
        neighbors_i = set(g.neighbors(i))
        neighbors_j = set(g.neighbors(j))

        intersection = neighbors_i.intersection(neighbors_j)
        union = neighbors_i.union(neighbors_j)

        if len(union) == 0:
            jaccard_coefficient = 0
        else:
            jaccard_coefficient = len(intersection) / len(union)
        print(f"Jaccard Coefficient between nodes {i} and {j}:")
        print(f"Jaccard Coefficient value: {jaccard_coefficient:.4f}")
        print("-" * 40)


