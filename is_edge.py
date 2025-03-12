# import igraph as ig
# import csv
#
# g = ig.Graph()
#
# g.add_vertices(34)
#
# with open("karate.edgelist", "r") as file:
#     edges = [tuple(map(int, line.strip().split())) for line in file]
#
# g.add_edges(edges)
#
#
# all_pairs = [(i, j) for i in range(34) for j in range(i + 1, 34)]
#
# with open("edges_presence.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Edge Exists"])
#
#     for pair in all_pairs:
#         node1, node2 = pair
#         edge_exists = 1 if g.are_adjacent(node1, node2) else 0
#         writer.writerow([edge_exists])



import igraph as ig
import numpy as np

# ایجاد گراف
g = ig.Graph()

# افزودن 34 گره به گراف
g.add_vertices(34)

# خواندن یال‌ها از فایل و افزودن آنها به گراف
with open("karate.edgelist", "r") as file:
    edges = [tuple(map(int, line.strip().split())) for line in file]

g.add_edges(edges)

# تعریف عامل تضعیف
beta = 0.5

# محاسبه ماتریس مجاورت
adj_matrix = np.array(g.get_adjacency().data)

# محاسبه معیار Katz برای کل گراف
I = np.identity(adj_matrix.shape[0])
katz_matrix = np.linalg.inv(I - beta * adj_matrix) - I

# استخراج مقادیر Katz فقط برای یال‌های موجود
katz_values_for_edges = []
for edge in edges:
    node_x, node_y = edge
    katz_value = katz_matrix[node_x, node_y]
    katz_values_for_edges.append(((node_x, node_y), katz_value))

# چاپ مقادیر Katz برای یال‌ها
temp = []
for edge, katz_value in katz_values_for_edges:
    temp.append(katz_value)
    print(f"Katz similarity for edge {edge}: {katz_value}")

import pandas as pd

# خواندن فایل CSV
df = pd.read_csv('updated_file2.csv')

df['Preferential Attachment'] = temp

# ذخیره‌ی تغییرات در فایل CSV
df.to_csv('data_updated3.csv', index=False)

print(len(katz_values_for_edges))