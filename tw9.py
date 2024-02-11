def next_day_date(d, m, y):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjusting for leap year
    if m == 2 and (y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
        month[1] = 29

    # Checking for invalid input
    if y <= 1812 or y > 2012 or d <= 0 or d > month[m - 1] or m < 1 or m > 12:
        return "Invalid Input"

    nd = d + 1
    nm = m
    ny = y

    if nd > month[m - 1]:
        nd = 1
        nm += 1

    if nm > 12:
        nm = 1
        ny += 1

    return nd, nm, ny

# Taking input
d, m, y = map(int, input("Enter the date, month, and year (in DD MM YYYY format): ").split())

# Calculating next day's date
next_day = next_day_date(d, m, y)

# Printing the result
if next_day == "Invalid Input":
    print("Invalid Input")
else:
    print("Given date is:", d, ":", m, ":", y)
    print("Next day's date is:", *next_day)