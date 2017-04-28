import time


class SortData:
    def __init__(self):
        self.start_time = time.time()

    def get_time(self, message):
        print('%s in %f seconds' % (message, time.time() - self.start_time))
        self.start_time = time.time()

    with open('input_file_large.txt', 'r') as input_file, open('sort_file_large.txt', 'w') as result_file:
        lines = input_file.readlines()
        get_time("read file finished")
        lines.sort()
        get_time("sort finished")
        result_file.writelines(lines)
        get_time('write result finished')


