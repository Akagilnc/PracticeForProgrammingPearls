import time


def get_time(start_time ,message):
    print('{message} in {time} seconds'.format(message=message, time=(time.time() - start_time)))

insert_list = []
start_time = time.time()
i = 0
with open('sort_file_large.txt', 'r') as file, open('formated_sorted_file.txt', 'w') as result_file:
    for line in file:
        if line == '\n':
            continue
        else:
            insert_list.append(line)

        if len(insert_list) > 10000000:
            get_time(start_time, "begin to write {line_num}".format(line_num=i))
            start_time = time.time()
            result_file.writelines(insert_list)
            insert_list.clear()
            get_time(start_time, "write finished {line_num}".format(line_num=i))
            start_time = time.time()
            i += 1