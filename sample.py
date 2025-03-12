import matplotlib.pyplot as plt
import igraph
g = igraph.Graph()

g.add_vertices(34)


with open("karate.edgelist", "r") as file:
    edges = [tuple(map(int, line.strip().split())) for line in file]

g.add_edges(edges)

print("Number of nodes:", g.vcount())
print("Number of edges:", g.ecount())


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



# انجام اجتماع‌یابی با الگوریتم Louvain
communities = g.community_multilevel()


modularity_value = communities.modularity


print(f"Modularity value: {modularity_value}")


for i, community in enumerate(communities):
    print(f"community{i + 1}: {community}")


num_communities = len(communities)
palette = igraph.drawing.colors.ClusterColoringPalette(num_communities)
community_colors = [palette[community] for community in communities.membership]


visual_style = {
    "vertex_size": 30,
    "vertex_color": community_colors,
    "vertex_label": range(g.vcount()),
    "vertex_label_size": 12,
    "vertex_label_color": "black",
    "edge_width": 2,
    "edge_color": "gray",
    "bbox": (400, 400),
    "margin": 30
}


layout = g.layout("kk")
fig, ax = plt.subplots()
igraph.plot(g, target=ax, layout=layout, **visual_style)
plt.show()