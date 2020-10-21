def remove_quotes(word):
    if word.startswith('\"') and word.endswith('\"'):
        word = word[1:-1]
    return word


def parse_row(row, delimiter):
    items = row.strip().split(sep=delimiter)
    if len(items) == 0:
        return items
    result = []
    nxt = ""
    for i, item in enumerate(items, 0):
        if (nxt.count("\"") % 2 == 0) and (i != 0):
            result.append(remove_quotes(nxt))
            nxt = item
        elif i == 0:
            nxt = item
        else:
            nxt = nxt + delimiter + item
    result.append(remove_quotes(nxt))
    return result


def read_csv(path_to_csv_file, delimiter=','):

    import os.path
    output = []

    if os.path.exists(path_to_csv_file):
        with open(path_to_csv_file, 'r') as my_csv:
            for line in my_csv:
                output += [parse_row(line, delimiter)]
        return output
    else:
        print("Error, such file doesn't exist")
        return []


def write_csv(path_to_csv_file, data, delimiter=','):

    if not isinstance(data[0], list):
        print('Cannot apply function, two-dimensional list required')

    elif type(path_to_csv_file) == str and path_to_csv_file == '':
        print('Path to file must be non-empty string')

    else:

        my_file = open(path_to_csv_file, 'w+')

        for row in data:
            for word in row:
                str_word = str(word)
                if delimiter in str_word:
                    str_word = '"' + word + '"'
                my_file.write(str_word)
                if word != row[-1]:
                    my_file.write(delimiter)
            my_file.write('\n')
        my_file.close()
