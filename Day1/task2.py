#Credit: https://www.reddit.com/r/adventofcode/comments/1883ibu/comment/kbj2stu/

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(text):
    for k, v in str2num.items():
        text = text.replace(k, v)
    return text

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
		text = file.read()

	text = replace_words(text)
	for line in text.split('\n')[:-1]:
			first_digit, last_digit = get_first_and_last_digit(line)
			value = int(f"{first_digit}{last_digit}")
			calibration_values.append(value)

	print(f"Sum: {sum(calibration_values)}")
