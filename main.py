import maps
from graph import Graph, Map
import networkx as nx

def main():
    m = Map(map=maps.map0)
    G = Graph(map=m)
    G.make_graph()
    print(nx.degree(G.mst))

    G.drawGraph()
    G.drawMST()
    G.show()

if __name__ == "__main__":
    main()