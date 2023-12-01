def get_first_and_last_digit(string):
	first_num, last_num = None, None
	for c in line:
		if c.isdigit():
			first_num = c
			break
	for c in reversed(line):
		if c.isdigit():
			last_num = c
			break
	return first_num, last_num

if __name__ == '__main__':
	calibration_values = []

	with open('input', 'r') as file:
		for line in file:
			first_digit, last_digit = get_first_and_last_digit(line)
			value = int(f"{first_digit}{last_digit}")
			calibration_values.append(value)

	print(f"Sum: {sum(calibration_values)}")

