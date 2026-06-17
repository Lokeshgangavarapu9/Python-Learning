import calendar

# 1. Ask the user for the year and month
year = int(input("Enter year (e.g., 2026): "))
month = int(input("Enter month (1-12): "))

# 2. Generate and print the formatted calendar
print("\n" + calendar.month(year, month))
print(calendar.calendar(year,month))
