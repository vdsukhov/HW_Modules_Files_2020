# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:57:17 2020

@author: Camille BENOIT
"""

def read_csv(path_to_csv_file, delimiter=",") :
    list_lines = []
    try :
        csv_f = open(path_to_csv_file, "r")
        for line in csv_f :
            this_line = line.split(delimiter)
            list_lines.append(this_line)
        return list_lines 
    except FileNotFoundError :
        print("Error, such file doesn't exist")
        return []
        
def write_csv(path_to_csv_file, data, delimiter=',') :
    if isinstance(path_to_csv_file, str) :
        if isinstance(data, list):
            if isinstance(delimiter, str) :
                with open(path_to_csv_file, "w") as out_f:
                    for line in data :
                        s = ""
                        for element in line :
                            if delimiter in element : 
                                s += "'"
                                s+= element
                                s+= "'"
                                s+= delimiter
                            else :
                                s += (element + delimiter)
                        s = s[:-1]
                        out_f.write(s +"\n")
            else : 
                print("Error : delimiter should be a string")
        else :
            print("Error : data sould be a list")
    else :
        print("Error : path_to_csv_file should be a string")

        