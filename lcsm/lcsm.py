import frequent_commands as fc

database = 'rosalind_lcsm.txt'
data = fc.fasta_to_dictionary(database)
memo = []

def lcm(memo, value):
    for substring in memo:
        if substring in value:
            pass
        else:
            memo.discard(substring)
    return memo

if len(data) == 1:
    print(next(iter(data.values())))
else:
    #do the thing for two
    # recurs
