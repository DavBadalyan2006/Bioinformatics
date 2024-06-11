def fasta_to_dictionary(database: str):
    with open(database, 'r') as file:
        sequences = {}
        current_key = None
        current_value = ''

        for line in file:
            if line.startswith('>'):
                if current_key is not None:
                    sequences[current_key] = current_value
                current_key = line.strip()[1:]
                current_value = ''
            else:
                current_value += line.strip()

        if current_key is not None:
            sequences[current_key] = current_value

    return sequences

def file_to_string(file: str):
    content = ""
    with open(file, 'r') as file:
        for line in file:
            content += line

    return content

