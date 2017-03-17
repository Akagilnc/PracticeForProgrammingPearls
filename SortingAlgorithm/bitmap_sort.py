import random


def bitmap_sort():
    index_list = []
    # Init the index and set all the element equal to 0
    for i in range(0, 10000000):
        index_list.append(0)

    # use +1 can make sure we won't miss some equals number.
    for line in open('input_file.txt', 'r'):
        index_list[int(line)] += 1

    # Open a file to write result
    f = open('result_file.txt', 'w')

    # Write result to file
    for index, value in enumerate(index_list):
        if value > 0:
            f.write((str(index)+'\n') * value)


def make_input():
    # Make 1000000 random number to input
    input_list = random.sample(range(1000000, 10000000),
                               8000000)

    f_input = open('input_file.txt', 'w')
    for line in input_list:
        f_input.write(str(line) + '\n')
    f_input.close()

# make_input()
bitmap_sort()

