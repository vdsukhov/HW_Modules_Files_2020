def read_csv(path_to_csv_file, delimiter=','):

	li_words = []
	try:
		with open(path_to_csv_file, 'r') as input_file:		
			for line in input_file:
				line = line.strip()
				words = []
				words_tmp = line.split(delimiter)
				i = 0
				while i < len(words_tmp):
					word = words_tmp[i]
					if word.count('"') == 1:
						word1 = word.strip('"')
						i += 1
						word2 = words_tmp[i].strip('"')
						word = word1 + delimiter + word2
					if word.count('"') == 2:
						word = word.strip('"')
					i += 1
					words.append(word)
				li_words.append(words)

	except Exception:
			print("Error, such file doesn't exist")

	return li_words

def write_csv(path_to_csv_file, data, delimiter=','):
	if type(data) != list:
		print("invalid csv: data is not a list")
		return

	ncols = len(data[0])
	for line in data:
		if len(line) != ncols:
			print("invalid csv: data has incomplete lines")
			return

	output_file = open(path_to_csv_file, 'w')
	for line in data:
		for item in line[:-1]:
			output_file.write(item)
			output_file.write(delimiter)
		output_file.write(line[-1])
		output_file.write('\n')
	output_file.close()
