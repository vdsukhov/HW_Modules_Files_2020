def read_csv(path_to_csv_file, delimiter=","):
    try:
        with open(path_to_csv_file) as inp:
            new_file = []
            for line in inp:
                line = line.strip()
                new_line = [i for i in line.split(delimiter)]
                if '"' in line:
                    word = ''
                    new_line_2 = []
                    for elem in new_line:
                        if elem[0] == '"' and elem[-1] == '"':
                            new_line_2.append(elem[1:(len(elem) - 1)])
                        elif elem[0] == '"':
                            word += elem[1:(len(elem))] + delimiter
                        elif elem[-1] == '"':
                            word += elem[0:(len(elem) - 1)]
                            new_line_2.append(word)
                            word = ''
                        elif len(word) != 0:
                            word += elem + delimiter
                        else:
                            new_line_2.append(elem)
                    new_line = new_line_2
                new_file.append(new_line)
        return new_file

    except FileNotFoundError:
        print("Error, such file doesn't exist")
        return []


def write_csv(path_to_csv_file: str, data: list, delimiter=','):
    if type(path_to_csv_file) != str or type(data) != list or type(delimiter) != str:
        print("Arguments: path_to_csv_file (str, create/rewrite file), data (list), delimeter (str: 'symbol')")
    else:
        with open(path_to_csv_file, "w") as file:
            for elem in data:
                for i in range(len(elem) - 1):
                    if delimiter in elem[i]:
                        file.write('"' + elem[i] + '"')
                    else:
                        file.write(elem[i] + delimiter)
                if delimiter in elem[-1]:
                    file.write('"' + elem[-1] + '"')
                else:
                    file.write(elem[-1])
                file.write('\n')




