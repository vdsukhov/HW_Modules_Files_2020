import mycsv
lines = mycsv.read_csv("data.csv",delimiter="*")
print(lines)

mycsv.write_csv("data_1.csv", lines)
mycsv.write_csv("data_1.tsv", lines,delimiter ="\t")
