import random
import string
import time


class MakeData:
    def __init__(self):
        self.start_time = time.time()

    def id_generator(self, size=4, chars=string.ascii_letters + string.digits + string.hexdigits):
        return ''.join(random.choice(chars) for _ in range(size))

    def get_number(self):
        return str(random.getrandbits(32))

    def get_time(self, message):
        print('%s in %f seconds' % (message, time.time() - self.start_time))
        self.start_time = time.time()

    def make_data(self):
        temp_list, p = [], 0.1
        # Open a input file to store these numbers
        # Write numbers to input_file
        for i in range(1001):
            for line in range(10**6):
                number = self.get_number()
                temp_list.append(str(number) + ',' + str(number) + 'Description \n')
            else:
                self.get_time("--- %f%% end ---" % p)
                p += 0.1

            with open('input_file_large.txt', 'a') as f_input:
                f_input.writelines(temp_list)
            self.get_time('write file end')
            temp_list.clear()

makedata = MakeData()
makedata.make_data()