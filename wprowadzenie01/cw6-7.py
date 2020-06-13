num_list = [x + 1 for x in range(10)]
new_list = num_list[5:]
num_list = num_list[:5]

num_list += new_list
num_list = [0] + num_list
list_copy = num_list.copy()
print(sorted(list_copy, reverse=True))
