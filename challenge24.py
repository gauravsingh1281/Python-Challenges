# Wap to find the year is leap year or not

year = int(input("Enter Year"))


def leapYearCheck(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} It is a leap year")
    else:
        print(f"{year} It is not a leap year")


leapYearCheck(year)
