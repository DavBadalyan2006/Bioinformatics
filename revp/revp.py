import frequent_commands as fc

def reverse_component(s):
    sc = ""
    for character in s[::-1]:
        if character == "T":
            sc += "A"
        elif character == "A":
            sc += "T"
        elif character == "C":
            sc += "G"
        elif character == "G":
            sc += "C"
    return sc


def find_reverse_palindromes(dna):
    palindromes = []
    sc = reverse_component(dna)
    sc = sc[::-1]
    for i in range(len(dna)):
        for length in range(4, min(13, len(dna)-i+1)):
            if dna[i:i+length] == (sc[i:i+length])[::-1]:
                palindromes.append((i+1, length))
    return palindromes



database = 'rosalind_revp.txt'
s = fc.fasta_to_dictionary(database)
dna = next(iter(s.values()))
sc = reverse_component(dna)
reverse_palindromes = find_reverse_palindromes(dna)
for pos, length in reverse_palindromes:
    print(f"{pos} {length}")