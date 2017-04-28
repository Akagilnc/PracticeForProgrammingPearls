import time


class SortData:
    def __init__(self):
        self.start_time = time.time()

    def get_time(self, message):
        print('%s in %f seconds' % (message, time.time() - self.start_time))
        self.start_time = time.time()

    @staticmethod
    def write_to_temp_file(lines):
        total = 4375000000
        temp_1, temp_2, temp_3, temp_4, temp_5, temp_6, temp_7, temp_8 = [], [], [], [], [], [], [], []
        for line in lines:
            if int((line.split(','))[0]) < total//8:
                temp_1.append(line)
            elif total // 8 <= int((line.split(','))[0]) < total // 8 * 2:
                temp_2.append(line)
            elif total // 8 * 2 <= int((line.split(','))[0]) < total // 8 * 3:
                temp_3.append(line)
            elif total // 8 * 3 <= int((line.split(','))[0]) < total // 8 * 4:
                temp_4.append(line)
            elif total // 8 * 4 <= int((line.split(','))[0]) < total // 8 * 5:
                temp_5.append(line)
            elif total // 8 * 5 <= int((line.split(','))[0]) < total // 8 * 6:
                temp_6.append(line)
            elif total // 8 * 6 <= int((line.split(','))[0]) < total // 8 * 7:
                temp_7.append(line)
            else:
                temp_8.append(line)

        with open('temp_file_1', 'a') as file1, open('temp_file_2', 'a') as file2, \
                open('temp_file_3', 'a') as file3, open('temp_file_4', 'a') as file4, \
                open('temp_file_5', 'a') as file5, open('temp_file_6', 'a') as file6, \
                open('temp_file_7', 'a') as file7, open('temp_file_8', 'a') as file8:
                file1.writelines(temp_1)
                file2.writelines(temp_2)
                file3.writelines(temp_3)
                file4.writelines(temp_4)
                file5.writelines(temp_5)
                file6.writelines(temp_6)
                file7.writelines(temp_7)
                file8.writelines(temp_8)

    def write_to_result(self):
        for i in range(1, 9):
            with open('temp_file_'+str(i), 'r') as file, open("sort_file_large.txt", 'a') as result_file:
                tuple_lines = []
                lines = file.readlines()
                self.get_time("read finished " + str(i))
                for line in lines:
                    line = line.split(',')
                    tuple_lines.append((int(line[0]), line[1].lstrip()))
                self.get_time("translate finished " + str(i))

                tuple_lines = sorted(tuple_lines, key=lambda num: num[0])
                self.get_time("sort finished " + str(i))

                lines.clear()
                for line in tuple_lines:
                    lines.append(str(line[0]) + ',' + line[1])
                self.get_time("translate back finished " + str(i))

                result_file.writelines(lines)
                self.get_time('write result finished ' + str(i))

    def main(self):
        with open('input_file_large.txt', 'r') as input_file:
            total_line_num = 8*10**9
            i = 1
            while True:
                lines = input_file.readlines(total_line_num // 4)
                self.get_time("read file finished " + str(i))
                self.write_to_temp_file(lines)
                self.get_time("write to temp " + str(i))
                i += 1
                if not lines:
                    break

        self.write_to_result()

    def main2(self):
        self.write_to_result()


sort = SortData()
sort.main()