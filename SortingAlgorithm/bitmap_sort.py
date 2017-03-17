import random


def bitmap_sort():
    index_list = []
    # Init the index and set all the element equal to 0
    for i in range(0, 10000000):
        index_list.append(0)

    # Make the value = 1 when the number in file.
    for line in open('input_file.txt', 'r'):
        index_list[int(line)] = 1

    # Open a file to write result
    with open('result_file.txt', 'w') as f:
        # Write result to file
        for index, value in enumerate(index_list):
            if value == 1:
                f.write((str(index)+'\n') * value)


def make_input():
    # Make 10,000,000 unique random number
    input_list = random.sample(range(1000000, 10000000),
                               8000000)

    # Open a input file to store these numbers
    with open('input_file.txt', 'w') as f_input:
        # Write numbers to input_file
        for line in input_list:
            f_input.write(str(line) + '\n')

# make_input()
bitmap_sort()

