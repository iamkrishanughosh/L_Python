list_of_integers = input("Enter : ").split()
highest = 0
lowest = int(list_of_integers[0])
for num in list_of_integers:
    num = int(num)
    if num > highest:
        highest = num
    if lowest > num:
        lowest = num

print(highest)
print(lowest)
