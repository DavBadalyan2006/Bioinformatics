import frequent_commands as fc

database = 'rosalind_dna.txt'
s = fc.file_to_string(database)
print(f"{s.count('A')} {s.count('C')} {s.count('G')} {s.count('T')}")
