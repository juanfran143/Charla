class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return self.name

    def __repr__(self):
        return "My name is " + self.name

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.year == other.year


if __name__ == '__main__':
    a = {"1": 3, "2": 2, "3": 1}

    d = {"Vero": 24, "Juanfran": 26, "Yuda": 32}
    sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    print(a)

    d = {1: Person("Vero", 24), 2: Person("Juanfran", 26), 3: Person("Yuda", 32)}
    print(d)

    d = {Person("Juanfran", 26): "Juanfran", Person("Juanfran", 26): "Juanfran", Person("Yuda", 32): "Yuda"}
    print(d)
