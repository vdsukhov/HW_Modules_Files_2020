import re

def splitter(line, delimiter):
    quote = True
    lresult = []
    lsplit_pos = [0]
    for pos, elem in enumerate(line):
        if elem == "\"":
            quote = not quote
        if elem == delimiter and quote:
            lsplit_pos.append(pos)
    lsplit_pos.append(len(line)+1)
    for i in range(len(lsplit_pos)-1):
        lresult.append(re.sub("^" + delimiter + "|\"", "", line[lsplit_pos[i]:lsplit_pos[i+1]]))
    return lresult


def read_csv(path_to_csv_file, delimiter=","):
    columns = []
    with open(path_to_csv_file, "r") as f:
        for line in f:
            if delimiter == "*":
                columns.append(line.strip('\n').replace('"', "").split(delimiter))
            else:
                columns.append(splitter(line.strip('\n'), delimiter))
    return columns


def write_csv(path_to_csv_file, data, delimiter=','):
    with open(path_to_csv_file, "w") as out_f:
        lresult = []
        for line in data:
            lline = []
            for elem in line:
                if delimiter in elem:
                    lline.append('"' + elem + '"')
                else:
                    lline.append(elem)
            lresult.append(delimiter.join(lline))
        out_f.writelines("\n".join(lresult))

def test():
    print('data_1')
    print(read_csv(r"C:\Users\yakup\PycharmProjects\python_hw4\data_1.csv"))
    print('data_2')
    print(read_csv(r"C:\Users\yakup\PycharmProjects\python_hw4\data_2.csv"))
    print('data_3')
    print(read_csv(r"C:\Users\yakup\PycharmProjects\python_hw4\data_3.csv", "*"))

    lst = read_csv(r"C:\Users\yakup\PycharmProjects\python_hw4\data_3.csv", "*")
    write_csv(r"C:\Users\yakup\PycharmProjects\python_hw4\data_3_1.tsv", lst, ",")
    write_csv(r"C:\Users\yakup\PycharmProjects\python_hw4\data_3_2.tsv", lst, "\t")


