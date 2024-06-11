import frequent_commands as fc
import itertools

database = 'rosalind_lexf.txt'
*alphabet, n = fc.file_to_string(database).split()

strings = itertools.product(alphabet, repeat=int(n))
for string in strings:
    print(''.join(string))
