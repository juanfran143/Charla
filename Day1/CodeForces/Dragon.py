# https://codeforces.com/problemset/problem/230/A

def can_defeat_all_dragons(s, n, dragons):
    # Sort the dragons based on their strength
    dragons.sort()

    # Loop through each dragon
    for xi, yi in dragons:
        if s > xi:
            # Kirito wins and gains bonus strength
            s += yi
        else:
            # Kirito loses
            return "NO"

    # Kirito defeats all dragons
    return "YES"


# Test the function with the given example
s = 2
n = 2
dragons = [(1, 99), (100, 0)]
can_defeat_all_dragons(s, n, dragons)