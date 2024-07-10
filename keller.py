year = int(input("Year: "))
while year < 1583 or year > 9999:
    print("Out of allowed range 1583 to 9999")
    year = int(input("Year: "))

month = int(input("Month: "))
while month < 1 or month > 12:
    print("Out of allowed range 1 to 12")
    month = int(input("Month: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day = int(input("Day: "))
    while day < 1 or day > 31:
        print("Out of allowed range 1 to 31")
        day = int(input("Day: "))
    
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = int(input("Day: "))
    while day < 1 or day > 30:
        print("Out of allowed range 1 to 30")
        day = int(input("Day: "))
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        day = int(input("Day: "))
        while day < 1 or day > 29:
            print("Out of allowed range 1 to 29")
            day = int(input("Day: "))
    else:
        day = int(input("Day: "))
        while day < 1 or day > 28:
            print("Out of allowed range 1 to 28")
            day = int(input("Day: "))

if month == 1 or month == 2:
    month += 12
    year -= 1

weekday = (day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
if weekday == 0:
    print("It is a Saturday!")
elif weekday == 1:
    print("It is a Sunday!")
elif weekday == 2:
    print("It is a Monday!")
elif weekday == 3:
    print("It is a Tuesday!")
elif weekday == 4:
    print("It is a Wednesday!")
elif weekday == 5:
    print("It is a Thursday!")
else: 
    print("It is a Friday!")
