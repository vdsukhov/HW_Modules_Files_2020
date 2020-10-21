from pathlib import Path

def read_csv(path_to_csv_file, delimiter=","):
    def _dlmiter(test_str):
        temp = ''
        res = []
        check = 0
        for ele in test_str:
            if ele == '"':
                check += 1
            if ele == delimiter and (check == 2 or check == 0):
                if temp.strip():
                    res.append(temp)
                temp = ''
            else:
                temp += ele
        if temp.strip():
            res.append(temp)
        return res

    if Path(path_to_csv_file).exists():
        fulllist = []
        pre_list = []
        ans = []
        filename = Path(path_to_csv_file)

        with open (filename) as f:
            read_data = f.readlines()
        for line in read_data:
            pre_list.append(line.strip('\n'))
        for k in pre_list:
            res = _dlmiter(k)
            fulllist.append(res)
        for i in range(len(fulllist)):
            for j in range(len(fulllist[i])):
                new_str=str(fulllist[i][j]).replace('"','')
                fulllist[i][j] = new_str

        return fulllist
    else:
        print("Error, such file doesn't exist")
        return []


def write_csv(path_to_csv_file, data, delimiter=','):
    if isinstance(path_to_csv_file,str) == True and path_to_csv_file !='':
        if isinstance(data,list) and isinstance(data[0],list):
            filename = Path(path_to_csv_file)
            with open(filename,'w+') as f:
                for item in data:
                    f.write(delimiter.join([str(x) for x in item]) + '\n')
            f.close()

        else:
            error = 'Error. Wrong type of data!'
            return error
    else:
        error = 'Incorrect call, please specify path to the file!'
        return error
