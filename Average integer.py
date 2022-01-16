numbers_list = input("Enter : ").split()
i = 0
no_of_integers = 0
for n in range(0, len(numbers_list)):
    numbers_list[n] = int(numbers_list[n])
    no_of_integers += 1
    i += numbers_list[n]

print(round(i/no_of_integers))
