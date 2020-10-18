def read_csv(path_to_file, delimiter=","):
    lines = []
    try:
        with open(path_to_file) as inp_f:
            for line in inp_f:
                lines.append(line.strip())
        final_words = [[] for i in range(len(lines))]
        quot_mark = False
        count_quot_mark = 0
        for i in range(len(lines)):
            word = []
            for j in range(len(lines[i])):
                if lines[i][j] == '"':
                    quot_mark = True
                    count_quot_mark += 1
                else:
                    if quot_mark:
                        word.append(lines[i][j])
                        if count_quot_mark == 2:
                            quot_mark = False
                    else:
                        if lines[i][j] != delimiter:
                            word.append(lines[i][j])
                        else:
                            final_words[i].append("".join(word))
                            word = []
            final_words[i].append("".join(word))
        return (final_words)

    except:
        print("Error, such file doesn't exist")
        return ([])


def write_csv(path_to_file, lines, delimiter=','):
    lines_tables = []
    del_ = delimiter
    for i in range(len(lines)):
            words = []
            for j in range(len(lines[i])):
                if del_ in lines[i][j]:
                    lines[i][j] = '"' + lines[i][j] + '"'
                words.append("".join(str(elem) for elem in lines[i][j]))
            lines_tables.append(delimiter.join(str(elem) for elem in words))
    try:
        with open(path_to_file, "w") as out_f:
            out_f.writelines("\n".join(str(elem) for elem in lines_tables))
    except:
        print("Error, incorrect call")




