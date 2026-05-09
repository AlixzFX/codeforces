# https://codeforces.com/problemset/problem/23/A

def solve():
    string = input()
    best = 0
    for offset in range(1, len(string)):
        for start in range(len(string)):
            i = 0
            while i + offset + start < len(string) and string[i + start] == string[i + offset + start]:
                i += 1

            if i > best:
                best = i

    print(best)

solve()