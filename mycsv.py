# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 02:22:35 2020
@author: Alexandra Giraud 

"""

path_to_csv_file = r"C:\Users\sacho\Documents\3A ITMO\Python\HW_Modules_Files_2020\data_1.csv"
def read_csv(path_to_csv_file,delimiter=","):
    '''
    reads the file and returns a list of lines
    by default, the delimiter is a comma
    '''
    liste = list() #final list of lines 
    try :
        with open(path_to_csv_file,'r') as inp_f:
            for line in inp_f:
                a = line.split(delimiter)
                for i in range(len(a)): #in case there are cotation marks
                    a[i] = a[i].replace('"','')
                a[-1]= a[-1].replace('\n','') #otherwise \n appears at the endof lines
                liste.append(a)
        return liste
    except FileNotFoundError : 
        print('Error,such file doesn t exist')
        return []

data = [
    ['ID', 'Vlalue'], 
    ['101', '10,5'], 
    ['102', '11'],
    ['103','11.5']
    ]

def write_csv(path_to_csv_file,data,delimiter = ','):
    '''
     This function should save data from data variable 
     to the file with name path_to_csv_file 
     using delimiter delimiter'''
    if isinstance(path_to_csv_file,str) and isinstance(data,list) and isinstance(delimiter,str): 
        #if the input isn't correct error messages will appear
        with open(path_to_csv_file,'w') as out_f:
            for line in data:
                #print(line)
                for elem in line:
                    #print(elem)
                    ligne = ''#empty string with the content of the line in data that will be written in the file 
                    if delimiter in elem: #problem if element such as "10,5"  if delimiter is the comma
                         ligne+= '"' + elem + '"' #we put in form "10,5"
                         ligne+= delimiter
                    else:
                        ligne+= (elem + delimiter)

                ligne = ligne[:-1] #no need for delimiter at the end of the line
                out_f.write(ligne + '\n')
    else : 
        print('Error, incorrect call\n')
        print('please check is the path to the file is the correct form : r"path\" \n')
        print('please check that the input data is in correct form - a list')
        print('please check that the delimiter is a string according to the form : delimiter="delimiter"')
        
 
