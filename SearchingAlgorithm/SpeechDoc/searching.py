

class Searching:

    def get_file_size(self, filename):
        with open(filename, 'rb+') as file:
            return file.seek(0, 2)

    def get_line(self, file):
        for line in file.readlines(50):
            line = line.decode("utf-8").split(',')
            if not line:
                continue
            if len(line) < 2:
                continue
            if not line[1].lstrip().startswith(line[0]) or (not line[0]):
                continue
            return line

    def final_search(self, file, number):
        for line in file:
            line = line.decode("utf-8").split(',')
            if not line:
                file.seek(-500, 1)
            if len(line) < 2 or not line[0]:
                continue
            if int(line[0]) != number:
                if int(line[0]) > number:
                    file.seek(-500, 1)
                # print(line[0])
                continue
            else:
                return line


    def search(self, number):
        position = 1
        file_name = 'formated_sorted_file.txt'
        size = self.get_file_size(file_name)
        i = 1
        with open(file_name, 'rb+') as file:
            while True:
                i += 1
                if size > 1 or size < -1:
                    size //= 2
                else:
                    break

                if 1000 > abs(size) > 0:
                    line = self.final_search(file, number)
                    print("{search_times} times searched, result is :".format(search_times=i))
                    print(line)
                    break
                else:
                    file.seek(size, position)
                    line = self.get_line(file)
                    # print("outside" + str(line) + "size = " + str(size))
                    if int(line[0]) == number:
                        print("{search_times} times searched, result is :".format(search_times=i))
                        print(line)
                        break
                    elif int(line[0]) > number:
                        if size > 0:
                            size = 0 - size
                    elif int(line[0]) < number:
                        size = abs(size)




searching = Searching()
search_list = [1636257924, 2933815618, 1703720283, 3308069424, 3017114546, 4251742345]
for key in search_list:
    searching.search(key)