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
        temp_1, temp_2, temp_3, temp_4, temp_5, temp_6, temp_7, temp_8, temp_9, temp_10, \
            temp_11, temp_12, temp_13, temp_14, temp_15, temp_16 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        for line in lines:
            if int((line.split(','))[0]) < total // 16:
                temp_1.append(line)
            elif total // 16 <= int((line.split(','))[0]) < total // 16 * 2:
                temp_2.append(line)
            elif total // 16 * 2 <= int((line.split(','))[0]) < total // 16 * 3:
                temp_3.append(line)
            elif total // 16 * 3 <= int((line.split(','))[0]) < total // 16 * 4:
                temp_4.append(line)
            elif total // 16 * 4 <= int((line.split(','))[0]) < total // 16 * 5:
                temp_5.append(line)
            elif total // 16 * 5 <= int((line.split(','))[0]) < total // 16 * 6:
                temp_6.append(line)
            elif total // 16 * 6 <= int((line.split(','))[0]) < total // 16 * 7:
                temp_7.append(line)
            elif total // 16 * 7 <= int((line.split(','))[0]) < total // 16 * 8:
                temp_8.append(line)
            elif total // 16 * 8 <= int((line.split(','))[0]) < total // 16 * 9:
                temp_9.append(line)
            elif total // 16 * 9 <= int((line.split(','))[0]) < total // 16 * 10:
                temp_10.append(line)
            elif total // 16 * 10 <= int((line.split(','))[0]) < total // 16 * 11:
                temp_11.append(line)
            elif total // 16 * 11 <= int((line.split(','))[0]) < total // 16 * 12:
                temp_12.append(line)
            elif total // 16 * 12 <= int((line.split(','))[0]) < total // 16 * 13:
                temp_13.append(line)
            elif total // 16 * 13 <= int((line.split(','))[0]) < total // 16 * 14:
                temp_14.append(line)
            elif total // 16 * 14 <= int((line.split(','))[0]) < total // 16 * 15:
                temp_15.append(line)
            else:
                temp_16.append(line)

        with open('temp_file_1', 'a') as file1, open('temp_file_2', 'a') as file2, \
                open('temp_file_3', 'a') as file3, open('temp_file_4', 'a') as file4, \
                open('temp_file_5', 'a') as file5, open('temp_file_6', 'a') as file6, \
                open('temp_file_7', 'a') as file7, open('temp_file_8', 'a') as file8, \
                open('temp_file_9', 'a') as file9, open('temp_file_10', 'a') as file10, \
                open('temp_file_11', 'a') as file11, open('temp_file_12', 'a') as file12, \
                open('temp_file_13', 'a') as file13, open('temp_file_14', 'a') as file14, \
                open('temp_file_15', 'a') as file15, open('temp_file_16', 'a') as file16:
            file1.writelines(temp_1)
            file2.writelines(temp_2)
            file3.writelines(temp_3)
            file4.writelines(temp_4)
            file5.writelines(temp_5)
            file6.writelines(temp_6)
            file7.writelines(temp_7)
            file8.writelines(temp_8)
            file9.writelines(temp_9)
            file10.writelines(temp_10)
            file11.writelines(temp_11)
            file12.writelines(temp_12)
            file13.writelines(temp_13)
            file14.writelines(temp_14)
            file15.writelines(temp_15)
            file16.writelines(temp_16)

    def write_to_result(self):
        for i in range(1, 17):
            with open('temp_file_' + str(i), 'r') as file, open("sort_file_large.txt", 'a') as result_file:
                tuple_lines = []
                lines = file.readlines()
                self.get_time("read finished " + str(i))
                for line in lines:
                    line = line.split(',')
                    tuple_lines.append((int(line[0]), line[1]))
                self.get_time("translate finished " + str(i))

                tuple_lines = sorted(tuple_lines, key=lambda tuple_line: tuple_line[0])
                self.get_time("sort finished " + str(i))

                lines.clear()
                for line in tuple_lines:
                    result_file.write(str(line[0]) + ',' + line[1] + '\n')
                self.get_time('write result finished ' + str(i))

    def main(self):
        with open('input_file_large.txt', 'r') as input_file:
            total_line_num = 8 * 10 ** 9
            i = 1
            while True:
                lines = input_file.readlines(total_line_num // 4)
                if not lines:
                    break

                self.get_time("read file finished " + str(i))
                self.write_to_temp_file(lines)
                self.get_time("write to temp " + str(i))
                i += 1


        self.write_to_result()

    def main2(self):
        self.write_to_result()


sort = SortData()
sort.main()
