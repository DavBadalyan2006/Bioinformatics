def mortal_fib(n, m, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2 or m == 1:
        return 1
    else:
        memo[n] = mortal_fib(n-1, m, memo) + mortal_fib(n-2, m, memo) - (mortal_fib(n-m-1, m, memo) if n - m > 0 else 0)
        return memo[n]


print(mortal_fib(96, 17))
