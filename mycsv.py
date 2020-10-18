def read_csv(path_to_csv_file, delimiter=","):
    from pathlib import Path
    path=path_to_csv_file
    myfile=Path(path)
    csvls=[]
    mycsv=[]
    if myfile.is_file():
        with open(path) as file:
            for line in file:
                rowstr=line.strip()
                rowls=[]
                for i in rowstr:
                    rowls.append(i)
                rowls.append(delimiter)
                csvls.append(rowls)
    else:
        print("Error, such file doesn't exist")
        return([])
    for i in range(len(csvls)):
        deliminds=[]
        capinds=[]
        lst=csvls[i]
        row=[]
        readyrow=[]
        prevind=0
        next_ind=0
        for j in range(len(lst)):
            if lst[j]==delimiter:
                deliminds.append(j)
            elif lst[j]=='"':
                capinds.append(j)
        capindsodd=capinds[::2]
        capindseven=capinds[1::2]
        next_ind=0
        for i in range(len(lst)):
            if i > next_ind:
                if i in capindsodd:
                    next_ind=capindseven[0]
                    capindseven.pop(0)
                if i in deliminds:
                    row.append(lst[prevind:i])
                    prevind=i+1
        for i in range(len(row)):
            newelem=''
            for z in row[i]:
                if z!='"':
                    newelem+=z
            readyrow.append(newelem)
        mycsv.append(readyrow)
    return(mycsv)
def write_csv(path_to_csv_file, data, delimiter=','):
    import os
    path=path_to_csv_file
    if os.path.exists(path):
        list_of_delimiters=['.',',']
        with open(path,'w') as file:
            for i in data:
                line=i
                if delimiter != ',':
                    strtowrite=delimiter.join(line)+"\n"
                    file.writelines(strtowrite)
                else:
                    listtowrite=[]
                    for i in range(len(line)):
                        word=line[i]
                        iscomma=0
                        for i in word:
                            if i in list_of_delimiters:
                                iscomma=1
                        if iscomma==0:
                            listtowrite.append(word)
                        else:
                            newword='"'+word+'"'
                            listtowrite.append(newword)
                    strtowrite=','.join(listtowrite)+"\n"
                    file.writelines(strtowrite)
    else:
        print("This path doesn't exist.")
        print("Creating a new file")
        list_of_delimiters=['.',',']
        with open(path,'w') as file:
            for i in data:
                line=i
                if delimiter != 'c':
                    strtowrite=delimiter.join(line)+"\n"
                    file.writelines(strtowrite)
                else:
                    listtowrite=[]
                    for i in range(len(line)):
                        word=line[i]
                        iscomma=0
                        for i in word:
                            if i in list_of_delimiters:
                                iscomma=1
                        if iscomma==0:
                            listtowrite.append(word)
                        else:
                            newword='"'+word+'"'
                            listtowrite.append(newword)
                    strtowrite=','.join(listtowrite)+"\n"
                    file.writelines(strtowrite)
