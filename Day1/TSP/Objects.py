import random


class Node:
    def __init__(self, id: int, x: float, y: float):
        self.id = id
        self.x = x
        self.y = y

    def distance(self, node_x):
        return ((node_x.x - self.x) ** 2 + (node_x.y - self.y) ** 2) ** (1 / 2)


class Edge:
    def __init__(self, node_x: Node, node_y: Node):
        self.node_x = node_x
        self.node_y = node_y
        self.distance = self.generate_distance()

    def generate_distance(self):
        return ((self.node_x.x - self.node_y.x)**2 + (self.node_x.y - self.node_y.y)**2)**(1/2)

    def __str__(self):
        return " " + str(self.node_x.id) + "-" + str(self.node_y.id)


class Instance:
    def __init__(self, num_nodes):
        self.nodes = [Node(i+1, random.random()*10, random.random()*10) for i in range(num_nodes)]
        self.edges = self.generate_edges_ii()
        # self.edges

    def generate_edges(self):
        edges = {}
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                edges[(i, j)] = Edge(self.nodes[i], self.nodes[j])

        return edges

    def generate_edges_ii(self):
        edges = {}
        for i in range(len(self.nodes)):
            edges[i] = {}
            for j in range(len(self.nodes)):
                edges[i] = {j: Edge(self.nodes[i], self.nodes[j])} | edges[i]

        return edges
