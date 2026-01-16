def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def day_of_year(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    if is_leap(year):
        days_in_month[1] = 29

    day_of_years = sum(days_in_month[:month - 1]) + day
    return day_of_years


def day_in_year(year):
    """Returns the total number of days in a given year."""
    return 366 if is_leap(year) else 365


def date_diff(date1, date2):
    """Calculates the total days between two dates (inclusive)."""
    # Splitting the "DD-MM-YYYY" string into integers
    d1, m1, y1 = map(int, date1.split("-"))
    d2, m2, y2 = map(int, date2.split("-"))

    # Case 1: Both dates are in the same year
    if y1 == y2:
        return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1

    # Case 2: Dates are in different years
    # 1. Days remaining in the first year (inclusive of d1)
    days = day_in_year(y1) - day_of_year(d1, m1, y1) + 1

    # 2. Add full years in between
    for year in range(y1 + 1, y2):
        days += day_in_year(year)

    # 3. Add days from the final year
    days += day_of_year(d2, m2, y2)

    return days

# Test cases
print(f"Day of year for 29-02-2024: {day_of_year(29, 2, 2024)}") # Output: 60
print(f"Total days between 25-12-1999 and 09-03-2000: {date_diff('25-12-1999', '9-3-2000')}") # Output: 76
print(f"Damn") # Output: 60