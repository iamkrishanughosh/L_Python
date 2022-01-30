list_of_integers = input("Enter : ").split()
# Took input as a String and used split method to convert to a list.
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
