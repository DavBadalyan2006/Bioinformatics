import frequent_commands as fc

database = 'rosalind_grph.txt'
sequence = fc.fasta_to_dictionary(database)
info = []

for key1, value1 in sequence.items():
    for key2, value2 in sequence.items():
        if key1 != key2:
            if value1[:3] == value2[-3:] and ([key2, key1] not in info) and ([key1, key2] not in info):
                info.append([key2, key1])
            elif value1[-3:] == value2[:3] and ([key1, key2] not in info) and ([key2, key1] not in info):
                info.append([key1, key2])

cleaned_output = ""
for index, value in enumerate(info):
    cleaned_output += f"{info[index][0]} {info[index][1]} \n"
print(cleaned_output)
