data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('File has been read over, there are total', len(data), 'records')

print(data[0])
print('---------------')
print(data[1])

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('the average length is', sum_len/len(data))