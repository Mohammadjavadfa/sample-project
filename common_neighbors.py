import matplotlib.pyplot as plt
import igraph
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
        common_neighbors = neighbors_i.intersection(neighbors_j)

        print(f"Common neighbors between nodes {i} and {j}: {common_neighbors} (Count: {len(common_neighbors)})")
#
layout = g.layout("kk")

visual_style = {
    "vertex_size": 30,
    "vertex_color": "lightblue",
    "vertex_label": range(g.vcount()),
    "vertex_label_size": 12,
    "vertex_label_color": "black",
    "edge_width": 2,
    "edge_color": "gray",
    "bbox": (400, 400),
    "margin": 30
}

fig, ax = plt.subplots()
igraph.plot(g, target=ax, layout=layout, **visual_style)
plt.show()