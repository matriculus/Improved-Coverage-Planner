import networkx as nx
from utils import *
from matplotlib import pyplot as plt


class Node:
    NODE_ID = 0

    def __init__(self, status=Status.FREE, pos=(0, 0)):
        self.id = self.NODE_ID
        Node.NODE_ID += 1
        self.status = status
        self.pos = pos

    def __str__(self):
        # return f"Node(id={self.id}, status={self.status}, pos={self.pos})"
        return f"Node{self.id}"

    def __repr__(self):
        return self.__str__()

    def markVisited(self):
        if self.status == Status.FREE:
            self.status = Status.VISITED


class Map:
    def __init__(self, map=[[0, 0], [0, 0]]):
        assert isinstance(map, list)
        self.setMap(map)

    def setMap(self, map):
        self.map = np.array(
            [
                [Node(status=column, pos=(i, j)) for j, column in enumerate(row)]
                for i, row in enumerate(map)
            ]
        )
        self.nodes = [node for row in self.map for node in row]
        self.height, self.width = self.getSize()

    def __str__(self):
        return str(self.map)

    def getSize(self):
        return self.map.shape

    def getNode(self, row, col):
        return self.map[row, col]

    def getStatus(self, row, col):
        return self.map[row, col].status

    def getStartPosition(self):
        node = [node for node in self.nodes if node.status == Status.START][0]
        return node.pos

    def applyPath(self, path):
        for row, col in path:
            self.markVisited(row, col)

    def markVisited(self, row, col):
        self.map[row, col].markVisited()

    def allVisited(self):
        return all([node.status for node in self.nodes])

    def isOccupied(self, rows, cols):
        return all([node.status == Status.OCCUPIED for node in self.map[rows, cols]])

    def getNeighbours(self, node):
        i, j = node.pos
        neighbours = []
        if i > 0:
            neighbours.append(self.map[i - 1, j])
        if i < self.height - 1:
            neighbours.append(self.map[i + 1, j])
        if j > 0:
            neighbours.append(self.map[i, j - 1])
        if j < self.width - 1:
            neighbours.append(self.map[i, j + 1])

        return neighbours


class Graph(nx.Graph):
    def __init__(self, map=None):
        nx.DiGraph.__init__(self)
        self.map = map

    def make_graph(self):
        edges = [
            (node, neighbour)
            for node in self.map.nodes
            for neighbour in self.map.getNeighbours(node)
        ]
        self.add_edges_from(edges)
        self.pos = {node: np.array(node.pos)*100 for node in self.nodes}
        self.mst = self.getMST()

    def getMST(self):
        return nx.minimum_spanning_tree(self)
    
    def drawGraph(self):
        nx.draw_networkx_nodes(self, self.pos, node_color="blue", node_size=100)
        nx.draw_networkx_edges(self, self.pos, edge_color="grey")
    
    def drawMST(self):
        nx.draw_networkx_edges(self.mst, self.pos, edge_color="black", width=3)

    def show(self):
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    from maps import map2

    m = Map(map=map2)
    G = Graph(map=m)
    G.make_graph()
    
    G.drawGraph()
    G.drawMST()
    G.show()
