import math
import frequent_commands as fc

database = 'rosalind_pmch.txt'
dict = fc.fasta_to_dictionary(database)
s = next(iter(dict.values()))
print(math.factorial(s.count('A')) * math.factorial(s.count('G')))