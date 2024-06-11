import constants
import frequent_commands as fc

amino_acid_masses = constants.amino_acid_masses
database = 'rosalind_prtm.txt'
s = fc.file_to_string(database)
total_weight = 0
for char in s:
    weight = amino_acid_masses.get(char)
    total_weight += weight

print(total_weight)