# https://codeforces.com/problemset/problem/1703/G


class tree:
    def __init__(self, method, capa, chest, key_cost, pather=None):
        self.method = method
        self.n_bad_keys = 0 if method == 1 else 1
        self.pather = pather
        self.capa = capa
        self.cost = self.total_cost(chest.copy(), key_cost)

    def total_cost(self, chest, key_cost):
        saldo = 0 if self.pather is None else self.pather.cost

        self.n_bad_keys = self.n_bad_keys if self.pather is None else self.n_bad_keys + self.pather.n_bad_keys
        for _ in range(self.n_bad_keys):
            chest[self.capa] = int(chest[self.capa] / 2)

        if self.method == 0: #Coger la llave falsa
            saldo += chest[self.capa]
        else:
            saldo = saldo - key_cost + chest[self.capa]

        return saldo


def algo(chest, key_cost):
    lim_old = [tree(1, 0, chest, key_cost), tree(0, 0, chest, key_cost)]
    lim_new = []
    for capa in range(len(chest)-1):
        lim_new = []
        best = -99999999
        for i in [1, 0]:
            for k in lim_old:
                new_branch = tree(i, capa+1, chest, key_cost, pather=k)
                if i == 1:
                    lim_new.append(new_branch)
                    if best == -99999999 or best <= new_branch.cost:
                        best = new_branch.cost
                elif i != 1:
                    if new_branch.cost >= best:
                        lim_new.append(new_branch)
        lim_old = lim_new.copy()

    if len(lim_new) != 0:
        d = [i.cost for i in lim_new]
        nodo = lim_new[d.index(max(d))]
        methods = []
        while nodo is not None:
            methods.insert(0, nodo.method)
            nodo = nodo.pather

        return methods, max(d)

    else:
        d = [i.cost for i in lim_old]
        nodo = lim_old[d.index(max(d))]
        methods = [nodo.method]

        return methods, max(d)


def read_input():
    num = int(input())
    for k in range(num):
        aux = input().split(" ")
        n_chest = int(aux[0])
        key_cost = int(aux[1])

        aux = input().split(" ")
        chest = []
        for i in range(n_chest):
            chest.append(int(aux[i]))
        print()
        method, max = algo(chest, key_cost)
        print("Method: " + str(method))
        print("Max: " + str(max))


if __name__ == "__main__":
    read_input()