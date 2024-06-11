import frequent_commands as fc
import constants

codon_table = constants.codon_table

database = 'rosalind_prot.txt'
s = fc.file_to_string(database)
protein = ""
for i in range(0, len(s), 3):
    codon = s[i:i+3]
    amino_acid = codon_table.get(codon, "")
    if amino_acid != "*":  # Stop codon
        protein += amino_acid
    else:
        break  # Stop codon encountered, terminate translation

print(protein)