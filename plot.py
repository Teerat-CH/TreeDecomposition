import matplotlib.pyplot as plt
import numpy as np

# Original data
edges = [21692, 7034, 23873, 223000, 179178]
name = ['']
runtime = {
    "NetworkX - Min Deg.": [14.7, 0.985, 16.1, 2111, 1634],
    "NetworkX - Min Fill-In": [223, 15.1, 226, 19463, 13855],
    "Dynamic Min Deg. - Heap": [2.88, 0.87, 5.1, 77, 27.1],
    "Dynamic Min Deg. - Dict": [33.5, 3.6, 30.6, 6228, 4762],
    "Static Min Deg. - Dict": [30.8, 4.71, 336, 30937, 4497]
}
degree = {
    "NetworkX - Min Deg.": [24, 22, 49, 104, 38],
    "NetworkX - Min Fill-In": [16, 20, 43, 71, 32],
    "Dynamic Min Deg. - Heap": [12, 20, 43, 98, 40],
    "Dynamic Min Deg. - Dict": [19, 23, 51, 95, 40],
    "Static Min Deg. - Dict": [111, 208, 876, 1998, 332]
}

nameMap = {
    21692: "California",
    7034: "Oldenburg",
    23873: "San Joaquin",
    223000: "San Francisco",
    179178: "North America"
}

data = degree

# Sort indices based on edges
sorted_indices = sorted(range(len(edges)), key=lambda i: edges[i])
sorted_edges = [edges[i] for i in sorted_indices]

# Sort data accordingly
sorted_data = {
    algo: [data[algo][i] for i in sorted_indices]
    for algo in data
}

# Plot setup
x = np.arange(len(sorted_edges))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots(figsize=(15, 4))

# Plot each algorithm's runtime
for i, (label, data) in enumerate(sorted_data.items()):
    y_vals = [np.nan if val is None else val for val in data]
    opacity = 0.9 if "Heap" in label else 0.3  # Full opacity for Heap only
    ax.bar(x + i * width, y_vals, width, label=label, alpha=opacity)

# Labeling
ax.set_ylabel('Treewidth (log scale)')
ax.set_xlabel('Location and number of Edges')
ax.set_title('Treewidth of the resulting tree vs. Number of edges')
ax.set_xticks(x + width * 1.5)

# Combine name and edge count for x-axis labels
sorted_labels = [f"{nameMap[edges[i]]}\n({edges[i]})" for i in sorted_indices]
ax.set_xticklabels(sorted_labels)
ax.set_yscale('log')
ax.set_ylim(0.1, max([max([v for v in vals if v is not None]) for vals in sorted_data.values()]) * 1.5)

ax.legend(ncol=3)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
