def sumWithPerfection(num, n):
    integer = int(num * (10 ** n)) / (10 ** n)
    if float(integer) != 0.0:
        return float(integer)


data = {"javascript": 17400000, "python": 15700000, "java": 14000000, "c/c++": 11000000, "c#": 10000000, "php": 7900000, "kotlin": 5000000, "visual development tools": 5000000, "swift": 3500000, "go": 3300000, "objective c": 2400000, "rust": 2200000, "ruby": 2100000, "dart": 1800000, "lua": 1400000,}
number = []

for element in data:
    # print("{}:{}".format(element, data[element]))
    number.append(data[element])

# print('---')
total = sum(number)
for element in range(len(number)):
    calcul = sumWithPerfection(100 * number[element] / total, 1)
    if calcul is not None:
        print("%s :" % (element + 1), "{}%".format(calcul))
