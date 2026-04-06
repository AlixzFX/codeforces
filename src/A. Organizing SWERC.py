def solve():
    n = int(input())
    D = {}
    for i in range(n):
        b, d = map(int, input().split())
        if d in D:
            if D[d] < b:
                D[d] = b
        else:
            D[d] = b
    tb = 0
    for i in range(1, 11):
        if not i in D:
            return print("MOREPROBLEMS")
        else:
            tb += D[i]
    return print(tb)

t = int(input())

for _ in range(t):
    solve()