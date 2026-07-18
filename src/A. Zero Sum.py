# https://codeforces.com/contest/2247/problem/A

def solve():
  n = int(input())
  a = list(map(int, input().split()))

  S = sum(a)

  if S == 0:
    return print("YES")

  if S % 2 != 0:
    return print("NO")

  if n <= abs(S):
    return print("NO")

  p = 0
  s = 1 if S > 0 else -1
  i = 0
  while i < n - 1:
    if a[i] == s and a[i + 1] == s:
      p += 1
      i += 2
    else:
      i += 1

  if p * 2 < abs(S):
    return print("NO")

  return print("YES")

  # solution :
  # if sum(a) % 4 == 0:
  #       print("YES")
  #   else:
  #       print("NO")

t = int(input())
for _ in range(t):
    solve()