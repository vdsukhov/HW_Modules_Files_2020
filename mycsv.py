# -*- coding: utf-8 -*-

# mycsv.py

def read_csv(path_to_csv_file, delimiter=","): 
    try:
        res = list()
        fileToRead = open(path_to_csv_file,"r")
        for line in fileToRead.readlines():
            res.append(line.split(delimiter)) 
        for i in range(len(res)): 
            for j in range(len(res[i])):
                res[i][j] = res[i][j].replace("\"","")
                res[i][j] = res[i][j].replace("\n","")
        return res
        fileToRead.close()
    except:
        print("Error, such file doesn't exist")

def write_csv(path_to_csv_file, data, delimiter=','): 
    try:
        fileToWrite = open(path_to_csv_file,"w")
        for line in data:
            for i in range(len(line)): # while there is an entry to add
                if i != (len(line) - 1): # it's no the last element on the line
                    fileToWrite.write(line[i] + delimiter)
                else: # It is the last element on the line so we add a new line jump instead of a separtor
                    fileToWrite.write(line[i] + "\n")
        fileToWrite.close()
    except:
        print("Error, such file can't be write")
