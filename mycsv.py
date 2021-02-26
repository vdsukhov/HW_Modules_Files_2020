
from pathlib import Path

#path_to_csv_file = '/home/maria/Documents/Python/data.csv' #path to file
#delimiter = ','

def read_csv(path_to_csv_file, delimiter=','):   
    if not Path(path_to_csv_file).is_file(): # if there is no such file
        print("Error, such file doesn't exist")
        return []

with open(path_to_csv_file) as our_file: 
    answ = []
    for line in our_file:  
        splitted = line.strip().split(delimiter)


        list_of_lines = []
        step = 0
        while step<len(splitted):
            if splitted[step].startswith('"') and splitted[step].endswith('"'):
                list_of_lines.append(splitted[step].strip('"'))
            elif splitted[step].startswith('"') and splitted[step].endswith(''):
                list_of_lines.append(splitted[step].strip('"') + delimiter + splitted[step+1].strip('"'))
                step += 2
            else:
                list_of_lines.append(splitted[step].strip())
            step += 1
            
        answ.append(list_of_lines)
    return(answ)

#path_to_csv_file = '/home/maria/Documents/Python/data.csv'
#data = [['ID', 'Vlaue'],[101, '10,5'], [102, 11],['103','11.5']]


def write_csv(path_to_csv_file, data, delimiter = 'c'):
    with open(path_to_csv_file, 'w') as out_f:
        for el in data:
            #print(el.map(str,el))
            out_f.writelines(delimiter.join(map(str,el)) + '\n')
    return(out_f)



