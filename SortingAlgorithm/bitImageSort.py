import random

indexList = []
inputList = []
# Make 1000000 random number to input
for i in range(0, 1000000):
    inputList.append(int(random.randrange(0, 10000000)))

# Init the index and set all the element equal to 0
for i in range(0, 10000000):
    indexList.append(0)

# use +1 can make sure we won't miss some equals number.
for num in inputList:
    indexList[num] += 1

# Open a file to write result
f = open('resultFile.txt', 'w')

# Write result to file
for i in range(10000000):
    if indexList[i] > 0:
        f.write((str(i)+'\n') * indexList[i])

f.close()

