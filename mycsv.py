def read_csv(path_to_csv_file, delimiter=","):
    import os
    if os.path.exists(path_to_csv_file) == False:
        print('Error, such file doesn\'t exist')
    else:    
        with open(path_to_csv_file, "r") as file:
            lines = []
            for line in file:
                line = line.strip()
                delim = [d for d in range(len(line)) if line.startswith(delimiter, d)]
                dquotes = [q for q in range(len(line)) if line.startswith('"', q)]
                to_remove = []
                for d in delim:
                    for q in dquotes[::2]:
                        if d > q and d < dquotes[dquotes.index(q) + 1]:
                            to_remove.append(d)
                for r in to_remove:
                    delim.remove(r)
                line = line.replace('"', '')               
                l = []
                l.append(line[:delim[0]])
                if len(delim) > 1:
                    for d in delim[:-1]:
                        l.append(line[d + 1:delim[delim.index(d) + 1]])
                l.append(line[delim[-1] + 1:])
                lines.append(l)            
            return(lines)
        
def write_csv(path_to_csv_file, data, delimiter=','):
    if not data:
        print('Error, data is empty')
    else:    
        with open(path_to_csv_file, "w+") as file:
            for line in data:
                for s in line:
                    if delimiter == ',' and (',' in s or '.' in s):
                        line[line.index(s)] = '"' + s + '"'
                dline = delimiter.join(line)
                file.writelines(dline)
                file.write('\n')
