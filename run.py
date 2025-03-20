import calendar

# Get user input for year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display the calendar
print("\n", calendar.month(year, month))