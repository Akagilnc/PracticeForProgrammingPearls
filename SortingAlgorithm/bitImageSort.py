import random

indexList = []
inputList = []

for i in range(0, 1000000):
    inputList.append(int(random.randrange(0, 10000000)))

for i in range(0, 10000000):
    indexList.append(0)

for num in inputList:
    indexList[num] += 1

f = open('resultFile.txt', 'w')

for i in range(10000000):
    if indexList[i] > 0:
        f.write((str(i)+'\n') * indexList[i])

f.close()

