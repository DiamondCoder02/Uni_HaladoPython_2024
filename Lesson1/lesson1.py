# Me comment, yay ^^

file = open("Lesson1/gaussian_log.txt", "r")
allTheText = []

for line in file:
	#for char in line:
	#    if char.isdigit():
	#        allTheText.append(line.strip())
	#        break
	if any(char.isdigit() for char in line):
		allTheText.append(line.strip())

# print(allTheText)

charges = []
for item in allTheText:
	if item[7] == "-":
		charges.append(float(item[7:15]))
	else:
		charges.append(float(item[8:15]))

# print(charges)

# LOL 2.exercise
import random
def lotto_get():
	for _ in range(50):
		pulledNums = set()
		while len(pulledNums) < 5:
			num = random.randint(1, 90)
			pulledNums.add(num)
		lotto = open("Lesson1/winNumbers.txt", "a")
		for item in pulledNums:
			print(item, end=" ", file=lotto)
		print("", file=lotto)

# lotto_get()


def lotto_calc():
	commonNums = {}
	lottoReadIn = open("Lesson1/winNumbers.txt", "r")
	for row in lottoReadIn:
		rowLine = row.strip().split(" ")
		for number in rowLine:
			if number in commonNums:
				commonNums[number] += 1
			else:
				commonNums[number] = 1
	print(commonNums)
	
	sortedDict = sorted(commonNums.items(), key=lambda item: item[1])
	print(sortedDict[-1:-6:-1])

	sortedReverse = sorted(commonNums.items(), key=lambda item: item[1], reverse=True)
	print(sortedReverse[:5])
	print(sortedReverse[-1:-6:-1])

lotto_calc()