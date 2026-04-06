n, x = map(int, input().split())
L = list(map(int, input().split()))

def solve():
    D = {}
    for i in range(n):
        if L[i] in D:
            return print(i + 1, D[L[i]] + 1)
        else:
            D[x - L[i]] = i
    return print("IMPOSSIBLE")

solve()
