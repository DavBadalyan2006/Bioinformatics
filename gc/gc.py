import frequent_commands as fc

def calculate_GC(s):
    count_C = s.count("C")
    count_G = s.count("G")
    return 100 * (count_C + count_G) / len(s)

database = 'rosalind_gc.txt'
sequences = fc.fasta_to_dictionary(database)

max_gc = 0
max_gc_index = None
for key, value in sequences.items():
    if max_gc < calculate_GC(value):
        max_gc = calculate_GC(value)
        max_gc_index = key
if max_gc_index:
    print(max_gc_index)
    print(f"{max_gc}")