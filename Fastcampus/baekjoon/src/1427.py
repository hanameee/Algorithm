data = input()
data_list = list()
for i in data:
    data_list.append(int(i))
data_list.sort(reverse=True)
joined_list = "".join(map(str, data_list))
print(int(joined_list))
