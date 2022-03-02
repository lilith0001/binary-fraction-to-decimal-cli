# handling input
binary = input("enter the binary string: ")
binary = binary.replace(" ","")
binsplit = binary.split('.')
valid = False
while not valid:
	if len(binsplit) < 3:
		flag = True
		for split in binsplit:
			if not flag:
				break
			for char in split:
				if char != '0' and char != '1':
					flag = False
					break
		if flag:
			valid = True
			break
	binary = input("invalid input. try again: ")
	binary = binary.replace(" ","")
	binsplit = binary.split('.')

# decimal conversion 
decimal = 0
power = 0
for digit in reversed(binsplit[0]):
	if digit != ' ':
		if int(digit) == 1:
			decimal += 2**power
		power += 1
if len(binsplit) > 1:
	power = -1
	for digit in binsplit[1]:
		if digit != ' ':
			if int(digit) == 1:
				decimal += 2**power
			power -= 1
print(f"decimal conversion: {decimal}")
