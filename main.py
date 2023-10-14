from maps import map2
from graph import Graph, Map

def main():
    m = Map(map=map2)
    G = Graph(map=m)
    G.make_graph()

    G.drawGraph()
    G.drawMST()
    G.show()

if __name__ == "__main__":
    main()