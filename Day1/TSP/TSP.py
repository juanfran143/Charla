from TSP import *
import random

class Solution:
    def __init__(self, instance):
        self.instance = instance
        self.solution = {"Route": [], "Distance": 0}

    def __build_random_solution(self):
        nodes = self.instance.nodes

        selected = random.choice(nodes)
        last = selected
        first = selected
        self.solution["Route"].append(selected)
        nodes.remove(selected)

        while len(nodes) > 0:
            selected = random.choice(nodes)
            self.solution["Route"].append(selected)
            self.solution["Distance"] += last.distance(selected)
            last = selected
            nodes.remove(selected)

        self.solution["Distance"] += last.distance(first)

    def __select_edge_greedy(self, sorted_edges):
        return list(sorted_edges.items())[0]

    def __get_possible_edges(self, node_id):
        return [i[1] for i in self.instance.edges.items() if i[0] == node_id][0]

    def __build_closest_neightboor(self):
        nodes = self.instance.nodes
        route = self.solution["Route"]
        route.append(nodes[0].id)

        possible_edges = self.__get_possible_edges(nodes[0].id)
        sorted_edges = {k: v for k, v in sorted(possible_edges.items(), key=lambda x: x[1].distance)}

        in_solution = True
        while in_solution and len(sorted_edges) > 0:
            in_solution = False
            selected_edge = self.__select_edge_greedy(sorted_edges)

            if selected_edge[0] in route:
                in_solution = True
                del sorted_edges[selected_edge[0]]
            else:
                pass

if __name__ == '__main__':
    pass
