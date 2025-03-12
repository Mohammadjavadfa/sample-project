import igraph as ig
import math
import csv

# ایجاد گراف
g = ig.Graph()

# افزودن 34 گره به گراف
g.add_vertices(34)

# خواندن یال‌ها از فایل و افزودن آنها به گراف
with open("karate.edgelist", "r") as file:
    edges = [tuple(map(int, line.strip().split())) for line in file]

g.add_edges(edges)


with open("results.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(["Node Pair", "Common Neighbors", "Jaccard Coefficient", "Preferential Attachment"])
    edgelist = g.get_edgelist()


    for edge in edgelist:
        i, j = edge
        neighbors_i = set(g.neighbors(i))
        neighbors_j = set(g.neighbors(j))

        #  Common Neighbors
        common_neighbors = neighbors_i.intersection(neighbors_j)
        common_neighbors_count = len(common_neighbors)

        #  Jaccard Coefficient
        intersection = neighbors_i.intersection(neighbors_j)
        union = neighbors_i.union(neighbors_j)
        jaccard_coefficient = len(intersection) / len(union) if len(union) != 0 else 0

        #  Preferential Attachment
        degree_i = len(g.neighbors(i))
        degree_j = len(g.neighbors(j))
        preferential_attachment = degree_i * degree_j

        writer.writerow([f"{i}-{j}", common_neighbors_count, jaccard_coefficient, preferential_attachment])

print("Results have been saved to 'results.csv'.")

# target
temp = []
edgelist = g.get_edgelist()
for edge in edgelist:
    node1, node2 = edge
    edge_exists = 1 if g.are_adjacent(node1, node2) else 0
    temp.append(edge_exists)

rows = []
with open("results.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)

new_column_name = "Target"

for i, row in enumerate(rows):
    row[new_column_name] = temp[i]

with open("updated_file.csv", "w", newline='') as csvfile:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        writer.writerow(row)
