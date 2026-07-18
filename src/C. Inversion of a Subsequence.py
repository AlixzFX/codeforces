# https://codeforces.com/contest/2247/problem/C

# solved !!!!

def solve():
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  if a == b:
    return print(0)

  diff = [a[i] - b[i] for i in range(n)]

  if all(not diff[i] or diff[i] == -1 for i in range(n)):
    if 1 in a and 0 in b:
      return print(2)
    return print(-1)

  if sum([a[i] if diff[i] else 0 for i in range(n)]) % 2 == 0:
    return print(2)
  else:
    return print(1)

t = int(input())
for _ in range(t):
    solve()