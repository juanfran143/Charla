from Day1.TSP.Objects import *
import random


class Solution:
    def __init__(self, instance):
        self.instance = instance
        self.solution = {"Route": [], "Distance": 0}

    def run(self):
        print("Random")
        self.__build_random_solution()
        self.__print_solution()

        print("Heuristic")
        self.__build_closest_neightboor()
        self.__print_solution()

    def __print_solution(self):
        print(self.solution["Route"])
        print(self.solution["Distance"])

    def __build_random_solution(self):
        nodes = self.instance.nodes.copy()

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
        return sorted_edges[0]

    def __get_possible_edges(self, node_id):
        route = self.solution["Route"]
        aux_1 = [i[1] for i in self.instance.edges.items() if i[0][0] == node_id and i[0][1] not in route]
        aux_2 = [i[1] for i in self.instance.edges.items() if i[0][1] == node_id and i[0][0] not in route]
        return aux_1 + aux_2

    def __build_closest_neightboor(self):
        nodes = self.instance.nodes

        self.solution["Route"] = []
        self.solution["Distance"] = 0

        route = self.solution["Route"]
        dist = self.solution["Distance"]

        route.append(nodes[0].id)

        while len(route) != len(nodes):
            possible_edges = self.__get_possible_edges(route[-1])
            sorted_edges = sorted(possible_edges, key=lambda x: x.distance)

            selected_edge = self.__select_edge_greedy(sorted_edges)

            if selected_edge.node_x.id in route and selected_edge.node_y.id in route:
                sorted_edges.remove(selected_edge)
            else:
                dist += selected_edge.distance
                if selected_edge.node_x.id in route:
                    route.append(selected_edge.node_y.id)
                else:
                    route.append(selected_edge.node_x.id)

        last_edge = self.instance.edges[(route[0], route[-1])]
        dist += last_edge.distance


if __name__ == '__main__':
    inst = Instance(5)
    sol = Solution(inst)
    sol.run()
