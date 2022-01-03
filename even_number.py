my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_list:
    if number % 2 == 0:
        print(f"Even {number}")
    else:
        print(f"Odd {number}")

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
# Float formatting to 3 places after decimal.
print(f"The sum of the list is {list_sum*0.1:1.3f}.")

