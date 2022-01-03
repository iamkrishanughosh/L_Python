year = int(input("Enter a year to check if leap year or not : "))


def leap_year_check(yearinput):
    if yearinput % 4 == 0:
        if yearinput % 100 != 0:
            print(f"Year {yearinput} is a leap year")
        else:
            if yearinput % 400 == 0:
                print(f"Year {yearinput} is a leap year")
            else:
                print(f"Year {yearinput} is not a leap year.")
    else:
        print(f"Year {yearinput} is not a leap year.")


leap_year_check(year)
