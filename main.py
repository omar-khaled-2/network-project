import networkx as nx
import heapq
import matplotlib.pyplot as plt
from tabulate import tabulate

G = nx.Graph()

with open('example.txt', 'r') as f:
    n = int(next(f).split(',')[1])
    for i in range(n):

        u, v, weight_str = next(f).strip().split(',')

        G.add_edge(u, v, weight=int(weight_str))



def single_source_dijkstra(graph,source):
    priority_queue = []
    heapq.heappush(priority_queue, (0, (source,None)))
    weights = {}
    links = {}
    logs = [];


    size = 1;


    for node in graph.nodes:
        weights[node] = float('inf')
        links[node] = None

    weights[source] = 0;
    links[source] = None


    while priority_queue:

        weight , item = heapq.heappop(priority_queue)
        node , link = item

        if weight > weights[node]:
            continue




        size = size - 1






        for _ , dest , data in graph.edges(node,data = True):

            w = weight + data["weight"]

            if w >= weights[dest]:
                continue
            l = link if link is not None and link != source else node
            weights[dest] = w;
            links[dest] = l
            size = size + 1
            heapq.heappush(priority_queue, (w, (dest,l)))
        logs.append((node,dict(weights),dict(links)))
    return weights , links , logs









for node in G.nodes:

    source = node;

    print("Source: ", node)

    weights , links , logs = single_source_dijkstra(G,source)

    nodes = [node for node in G.nodes if node != source]

    headers = ["Step","N"] + [f"D({node}),p({node})" for node in nodes]

    data = []

    for i in range(len(logs)):
        node,weights,links = logs[i]
        data.append([
            str(i),
            ("" if i == 0 else data[i - 1][1]) + node,


        ] + [(f"{weights[n]},{links[n]}" if weights[n] != float('inf') else str(weights[n]))for n in nodes])

    print(tabulate(data, headers=headers,tablefmt = "grid"))
    print("\n")

    headers = ["Destination", "Link"]
    data = [[node,f"({source},{links[node]})"] for node in nodes]
    print(tabulate(data, headers=headers,tablefmt = "grid"))

    print(2 * "\n")







pos = nx.circular_layout(G)




edge_labels = {(u, v): data['weight'] for u, v, data in G.edges(data=True)}

nx.draw_networkx_nodes(G, pos, node_size=500, node_color="blue",alpha = .7)
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_labels(G, pos,font_color="white")
nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels)


plt.show()
