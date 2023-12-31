from Day1.TSP.Objects import *
import random
import matplotlib.pyplot as plt


class Solution:
    def __init__(self, instance):
        self.instance = instance
        self.solution = {"Route": [], "Distance": 0}

    def run(self, verbose=False, plot=False):
        print("")
        print("Random")
        self.__build_random_solution()
        self.__print_solution(verbose)
        self.__plot_solution(plot)
        random_algo = self.solution["Distance"]

        print("Heuristic")
        self.__build_closest_neightboor()
        self.__print_solution(verbose)
        self.__plot_solution(plot)
        heuristic_algo = self.solution["Distance"]

        return random_algo, heuristic_algo

    def __plot_solution(self, plot, name="solution"):
        if plot:
            nodes = self.instance.nodes
            route = self.solution["Route"]
            x_coords = [nodes[i].x for i in route]
            y_coords = [nodes[i].y for i in route]

            # Añadir el primer nodo al final para cerrar el ciclo
            x_coords.append(nodes[route[0]].x)
            y_coords.append(nodes[route[0]].y)

            # Graficar
            plt.figure(figsize=(8, 8))
            plt.scatter(x_coords, y_coords, c='blue', label='Nodos')
            plt.plot(x_coords, y_coords, c='red', linestyle='-', linewidth=1, label='Ruta')
            plt.title('Representación de la Ruta')
            plt.xlabel('Coordenada X')
            plt.ylabel('Coordenada Y')
            plt.legend()
            plt.savefig(name+".png")
            plt.grid(True)
            plt.show()


    def __print_solution(self, verbose):
        if verbose:
            print(self.solution["Route"])
            print(self.solution["Distance"])

    def __build_random_solution(self):
        nodes = self.instance.nodes.copy()

        selected = random.choice(nodes)
        last = selected
        first = selected
        self.solution["Route"].append(selected.id)
        nodes.remove(selected)

        while len(nodes) > 0:
            selected = random.choice(nodes)
            self.solution["Route"].append(selected.id)
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

        route = self.solution["Route"]
        dist = 0

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

        self.solution["Distance"] = dist

    def __local_search_same_route(self):
        # 0-6-30-17-19-32
        route = self.solution["Route"]
        improve = True
        # edges = [Edge(self.instance.nodes[route[i]], self.instance.nodes[route[i+1]]) for i in range(len(route)-1)]
        while improve:
            improve = False
            edges = [Edge(self.instance.nodes[route[i]], self.instance.nodes[route[i+1]]) for i in range(len(route)-1)]
            for i in range(len(edges) - 2):
                for j in range(i + 1, len(edges) - 1):
                    x_i, y_i, z_i = edges[i].node_x, edges[i].node_y, edges[i + 1].node_y
                    x_j, y_j, z_j = edges[j].node_x, edges[j].node_y, edges[j + 1].node_y
                    if j == i + 1:
                        original_edge = edges[i].distance + edges[j + 1].distance
                        proposal_edge = y_i.distance(z_j) + y_j.distance(x_i)

                        if round(proposal_edge, 2) < round(original_edge, 2):
                            improve = True
                            edges[i] = Edge(x_i, y_j)
                            edges[i + 1] = Edge(y_j, y_i)
                            edges[j + 1] = Edge(y_i, z_j)
                            route = [i.node_x.id for i in edges] + [edges[-1].node_y.id]
                            self.solution["Distance"] += proposal_edge - original_edge

                    else:
                        original_edge = edges[i].distance + edges[i + 1].distance + edges[j].distance + \
                                        edges[j + 1].distance
                        proposal_edge = y_i.distance(x_j) + y_i.distance(z_j) + y_j.distance(x_i) + \
                                        y_j.distance(z_i)

                        if round(proposal_edge, 2) < round(original_edge, 2):
                            improve = True
                            edges[i] = Edge(x_i, y_j)
                            edges[i + 1] = Edge(y_j, z_i)
                            edges[j] = Edge(x_j, y_i)
                            edges[j + 1] = Edge(y_i, z_j)
                            route = [i.node_x.id for i in edges] + [edges[-1].node_y.id]
                            self.solution["Distance"] += proposal_edge - original_edge

        self.solution["Route"] = route

    def run_greedy_with_ls(self, verbose=False, plot=False, local_search=True):
        print("Heuristic")
        self.__build_closest_neightboor()
        self.__print_solution(verbose)
        self.__plot_solution(plot, name="Heuristic")
        if local_search:
            print("Local search")
            self.__local_search_same_route()
            self.__print_solution(verbose)
            self.__plot_solution(plot, name="LS")


if __name__ == '__main__':

    random_sol = []
    heuristic_sol = []
    for _ in range(1):
        inst = Instance(80)
        sol = Solution(inst)
        sol.run_greedy_with_ls(verbose=True, plot=True, local_search=True)

    """
    for _ in range(5):
        inst = Instance(5)
        sol = Solution(inst)
        random_algo, heuristic_algo = sol.run_greedy_with_ls(verbose=True)
        random_sol.append(random_algo)
        heuristic_sol.append(heuristic_algo)
    
    plt.figure(figsize=(8, 6))
    plt.boxplot([heuristic_sol, random_sol], labels=['Heuristic Solution', 'Random Solution'])
    plt.title('Boxplot de Soluciones Heurísticas y Aleatorias')
    plt.ylabel('Valor')
    plt.xlabel('Tipo de Solución')
    plt.grid(True)
    plt.show()
    """
