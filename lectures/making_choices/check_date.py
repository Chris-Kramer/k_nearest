def format_date(year,month,day):
    """
    returns a string with the date in the format yyyy-mm-dd.
    """
    return str(year) + '-' + str(month) + '-' + str(day)

def days_in_month(year,month):
    """
    returns the number of days in the given month.

    Precondition: 1 <= month <= 12
    """
    if (month == 4 or # April
        month == 6 or # June
        month == 9 or # September
        month == 11): # November
        return 30
    elif month == 2: # February
        if is_leap_year(year):
            return 29
        else:
            return 28
    else: # remaining months
        return 31
    
def is_leap_year(year):
    """
    returns True if the given year is a leap year and False otherwise.
    """
    # A year is a leap year if it is divisible by 400 or by 4 unless it is divisible by 100
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

print('This program checks if a numeric date is valid.')
year = int(input('Enter an integer for the year: '))
month = int(input('Enter an integer for the month: '))
day = int(input('Enter an integer for the day: '))
# no checks on year
# month needs to be between 1 and 12
if 1 <= month <= 12:
    # day needs to be between 1 and the number of days in the given month
    if 1 <= day <= days_in_month(year,month):
        print(format_date(year,month,day) + ' is valid.')
    else:
        print(format_date(year,month,day) +
              ' is not valid: the day must be between 1 and ' +
              str(days_in_month(year,month)) + '.')
else:
    print(format_date(year,month,day) +
          ' is not valid: the month must be between 1 and 12.')

# The program is complete. The next instruction is to keep it open when run using Python Launcher.
input('\nPress enter to terminate the program.')
