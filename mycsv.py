def read_csv(path_to_csv_file, delimiter=","):
  try:
    lines=[]
    with open (path_to_csv_file) as inp_f:
      for line in inp_f:
        new=[]
        line=line.strip()
        c=line.find('"')
        linen=line.split('"')
        if c == -1:
          new+=line.split(delimiter)
        else:
          for elem in linen:
            if len(elem)==0:
              continue
            elif elem[-1] == delimiter or elem[0] == delimiter:
              newelem=elem.split(delimiter)
            else:
              newelem=[elem]
            new+=newelem
        new1=list(filter(None,new))
        lines.append(new1)
  except FileNotFoundError:
    print("Error, such file doesn't exist")
  return lines

def write_csv(path_to_csv_file, data, delimiter=','):
  if type(data) != list:
    print('Incorrect call')
    return
  newdata=str()
  for elem in data:
    if delimiter == ',':
      for j in elem:
        if j.find(',') != -1 or j.find(".") != -1:
          i=elem.index(j)
          elem.remove(j)
          j='"'+j+'"'
          elem.insert(i, j)
    new=delimiter.join(elem)
    newdata+=new+'\n'
  with open(path_to_csv_file, "w") as out_f:
    out_f.write(newdata[:-1])
