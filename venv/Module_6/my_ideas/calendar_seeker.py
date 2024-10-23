import calendar


def year_full_calendars(year):
    print(f'This is the calendar of {year}')
    print(calendar.calendar(year))


def calendar_of_year_and_month(year, month):
    print(f'This is the calendar of year {year} of month {month}')
    print(calendar.month(year, month))


choice = int(input(
                   'Type 1 to seek the full calendar of an year'
                   'or type 2 to seek the month calendar of an year'
                   ))

if choice == 1:
    year = int(input('Type the year here: '))
    year_full_calendars(year)
else:
    year = int(input('Type the year here: '))
    month = int(input('Type the month here: '))
    calendar_of_year_and_month(year, month)
