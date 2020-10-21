import sys

def read_csv(path_to_csv_file, delimiter=","):
    res = []
    try:
        with open(path_to_csv_file, 'r') as f:
            for line in f:
                words = line.split(delimiter)
                res.append(words)
            res = [[s.strip() for s in nested] for nested in res]
            return res
    except IOError:
        print("Error, such file doesn't exist")
        return res


def write_csv(path_to_csv_file, data, delimiter=','):
    point = "."
    virg = ","
    try:
        with open(path_to_csv_file, "w+") as file:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if delimiter == "," and (point in data[i][j] or virg in data[i][j]):
                        data[i][j] = '"' + data[i][j] + '"'
                newline = delimiter.join(data[i])
                file.writelines(newline)
                file.write('\n')
    except FileNotFoundError:
        print("Error, incorrect call")