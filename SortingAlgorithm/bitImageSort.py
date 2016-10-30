import random

dict = []
list = []

for i in range(0, 1000000):
    list.append(int(random.randrange(0, 10000000)))

for i in range(0, 10000000):
    dict.append(0)

for num in list:
    dict[num] += 1

f = open('resultFile.txt', 'w')

for i in range(10000000):
    if dict[i] > 0:
        f.write((str(i)+'\n')*dict[i])

f.close()

