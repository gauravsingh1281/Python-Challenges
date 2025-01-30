# Wap to find the year is leap year or not

year = int(input("Enter Year"))


def leapYearCheck(year):
    # 1st way

    #     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    #         print(f"{year} It is a Leap Year")
    #     else:
    #         print(f"{year} It is not a Leap Year")

    # 2nd way

    if year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} It is a Leap Year")
        else:
            if year % 400 == 0:
                print(f"{year} It is a Leap Year")
            else:
                print(f"{year} It is not a Leap Year")
    else:
        print(f"{year} It is not a Leap Year")


leapYearCheck(year)
