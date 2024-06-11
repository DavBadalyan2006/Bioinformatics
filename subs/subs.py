import frequent_commands as fc

database = 'rosalind_subs.txt'
s, t = (fc.file_to_string(database)).split()
result = []

if len(t) <= len(s):
    for i in range(0, len(s) - len(t)):
        if s[i:i + len(t)] == t:
            result.append(i + 1)
    print(" ".join(str(char) for char in result))

