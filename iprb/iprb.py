""" Sample Output
0.78333
"""

k, m, n = map(int, input().split())
k = max(k, 0)
m = max(m, 0)
n = max(n, 0)
total_bonds = max((k + m + n) * (k + m + n - 1) / 2, 0)

