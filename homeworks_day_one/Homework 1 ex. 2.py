cube_list = []

for number in range (1, 1000, 2):
    cube = number ** 3
    cube_list.append(cube)

result_sum = 0
for element in cube_list:
    num_sum = 0
    test_element = element
    while test_element != 0:
        num_sum += test_element % 10
        test_element = test_element // 10

    if num_sum % 7 == 0:
        result_sum += num_sum

result_sum_changed = 0
for elem in cube_list:
    test_element = elem + 17
    num_sum = 0
    while test_element != 0:
        num_sum += test_element % 10
        test_element = test_element // 10
    if num_sum % 7 == 0:
        result_sum_changed += num_sum

print('Result of first list:' + (str(result_sum)))
print('Result of changed list:' + (str(result_sum_changed)))




