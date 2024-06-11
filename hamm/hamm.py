import frequent_commands as fc

def dH(s: str, t: str):
    dh = 0
    for i, j in zip(s, t):
        if i != j:
            dh += 1

    return dh

s, t = (fc.file_to_string('rosalind_hamm.txt')).split()
print(dH(s, t))

