def read_csv(path_to_csv_file, delimiter=","):
	try:
		f = open(path_to_csv_file)
	except:
		print("Error, such file doesn't exist")
		return []

	out = f.read().split()
	f.close()
	print(out)
	i = 0
	while True:
		#print(i)
		out[i] = out[i].split(delimiter)
		check = False
		#print(i, out)
		for j in range(len(out[i])):
			#print(i, out[i], len(out[i]))
			if out[i][j].startswith('"'):
				start = j
				#if out[i][j].endswith('"'):
				#out[i][start] = delimiter.join
				
				#out[i][j] = delimiter.join([out[i][j], out[i][j+1]]).strip('"')

				check = True
				#print(out[i])
			if check:
				if out[i][j].endswith('"'):
					if j == start:
						out[i][j] = out[i][j].strip('"')
					else:
						out[i][start] = delimiter.join(out[i][start:j+1]).strip('"')
						for m in range(start+1,j+1):
							out[i].pop(m)
					check = False

		i += 1
		if i==len(out):
			break
	return out


#print(read_csv('exampe.csv', '*'))
lines = [
    ['ID', 'Value'], 
    ['101', '10,5'], 
    ['102', '11'],
    ['103','11.5']
    ]


def write_csv(path_to_csv_file, data, delimiter=','):

	if not delimiter.isspace():
		for i in range(len(data)):
			#print(data[i])
			for j in range(len(data[i])):
				#print(data[i][j])
				if not data[i][j].isalnum():
					data[i][j] = ''.join(['"', data[i][j], '"'])
			
	for i in range(len(data)):
		data[i] = delimiter.join(data[i])
		#print(data)
	data = '\n'.join(data)
	print(data)
	with open(path_to_csv_file, 'w') as f:
		f.write(data)

#write_csv('e.csv', lines, '\t')