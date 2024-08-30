import matplotlib.pyplot as plt
import networkx as nx


def plot(nodes, edges, edge_labels):
    "given the nodes, edges, edge_labels provided by LLM, plot the knowledge grap   h"
    G = nx.Graph()
    G.add_edges_from(edges)

    lookup = {
        "Person": "#d32f2f",
        "Location": "#0277bd",
        "Event": "#e64980",
        "Role": "#757575"
    }
    node_color = []
    for node in G.nodes():
        if node in nodes:
            node_type = nodes[node]
            node_color.append(lookup.get(node_type, "#7e57c2"))
        else:
            node_color.append("#7e57c2")

    pos = nx.spring_layout(G)
    plt.figure(3,figsize=(15, 15))
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=50, node_color=node_color, alpha=0.9,
        font_size=6,
        labels={node: node for node in G.nodes()}
    )
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_size=6,
        font_color='red'
    )
    plt.axis('off')
    plt.show()
