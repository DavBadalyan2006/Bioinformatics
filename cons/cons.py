import frequent_commands as fc


def dna_matrix_to_profile(dna_matrix):
    profile = {'A': [0] * len(next(iter(dna_matrix.values()))),
               'C': [0] * len(next(iter(dna_matrix.values()))),
               'G': [0] * len(next(iter(dna_matrix.values()))),
               'T': [0] * len(next(iter(dna_matrix.values())))}

    for sequence in dna_matrix.values():
        for index, base in enumerate(sequence):
            profile[base][index] += 1

    return [profile[base] for base in "ACGT"]

def print_profile(profile: list[list[int]]):
    for base, counts in zip("ACGT", profile):
        line = f"{base}: {' '.join(str(count) for count in counts)}"
        print(line)


def profile_to_consensus(profile: list[list[int]]):
    consensus = ""
    for counts in zip(*profile):
        max_count = max(counts)
        if counts.count(max_count) == 1:
            consensus += "ACGT"[counts.index(max_count)]
    return consensus



database = 'rosalind_cons.txt'
dna_dict = fc.fasta_to_dictionary(database)
profile = dna_matrix_to_profile(dna_dict)
consensus = profile_to_consensus(profile)
print(consensus)
print_profile(profile)
