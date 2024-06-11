def rabbit(n, k, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = rabbit(n - 1, k, memo) + rabbit(n - 2, k, memo) * k
        return memo[n]

print(rabbit(32, 5))

