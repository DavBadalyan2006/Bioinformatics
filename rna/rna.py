import frequent_commands as fc

database = 'rosalind_rna.txt'
s = fc.file_to_string(database)
s = s.replace("T", "U")
print(s)
