import networkx as nx
import heapq
import matplotlib.pyplot as plt

G = nx.DiGraph()

with open('example.txt', 'r') as f:
    n = int(next(f).split(',')[1])
    for i in range(n):

        u, v, weight_str = next(f).strip().split(',')

        G.add_edge(u, v, weight=int(weight_str))



def single_source_dijkstra(graph,source):
    priority_queue = []
    heapq.heappush(priority_queue, (0, (source,[source])))
    lengths = {}
    paths = {}


    for node in graph.nodes:
        lengths[node] = float('inf')
        paths[node] = []



    while priority_queue:
        length , item = heapq.heappop(priority_queue)
        node , path = item
        print(item)


        if length >= lengths[node]:
            continue

        lengths[node] = length;
        paths[node] = path


        for _ , dest , data in graph.out_edges(node,data = True):
            heapq.heappush(priority_queue, (data["weight"] + length, (dest,path + [dest])))
        print(priority_queue);
        print("\n")
    return lengths , paths





single_source_dijkstra(G,"u")

for node in G.nodes:

    source = node;

    print("Source: ", node)
    weights , links = single_source_dijkstra(G,source)

    for link in links:
        if(link == source):
            continue
        print(link,links[link],weights[link])
    print("\n")





pos = nx.circular_layout(G)




edge_labels = {(u, v): data['weight'] for u, v, data in G.edges(data=True)}

nx.draw_networkx_nodes(G, pos, node_size=500, node_color="blue",alpha = .7)
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_labels(G, pos,font_color="white")
nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels)


plt.show()
