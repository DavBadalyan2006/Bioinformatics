def permutations(n):
    if n == 1:
        return [[1]]
    else:
        perms = permutations(n-1)
        result = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perm = perm[:i] + [n] + perm[i:]
                result.append(new_perm)
        return result

n = int(input().strip())
all_perms = permutations(n)
total_perms = len(all_perms)
print(total_perms)
for perm in all_perms:
    print(" ".join(map(str, perm)))