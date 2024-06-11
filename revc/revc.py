import frequent_commands as fc

database = 'rosalind_revc.txt'
s = fc.file_to_string(database)


def reverse_component(s: str):
    sc = ""
    for character in s[::-1]:
        if character == "T":
            sc += "A"
        elif character == "A":
            sc += "T"
        elif character == "C":
            sc += "G"
        elif character == "G":
            sc += "C"
    return sc


sc = reverse_component(s)

print(sc)
