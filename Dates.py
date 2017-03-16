#Ismael Garrido Dates.py
#inputs a date and outputs how many days into the year it is.

import calendar
def main():
    
    print('This program computes the number of days of an specific date')
    print()
    month = eval(input('Please enter the month number: '))
    day = eval(input('Please enter the day: '))
    days = numberOfDays(month) + day 
    print( calendar.month_name[month], str(day)+'th')
    print("The number of days in the year is:", days)
    numberOfDays(month)

    
def numberOfDays(month):

    if month == 1:
        return (0)
    elif month == 2:
        return (31)
    elif month == 3:
        return (59)
    elif month == 4:
        return (90)
    elif month == 5:
        return (120)
    elif month == 6:
        return (151)
    elif month == 7:
        return (181)
    elif month == 8:
        return (212)
    elif month == 9:
        return (243)
    elif month == 10:
        return (273)
    elif month == 11:
        return (303)
    elif month == 12:
        return (334)
    else:
        print("Please enter a valid month")


main()

"""
This program computes the number of days of an specific date

Please enter the month number: 12
Please enter the day: 31
December 31th
The number of days in the year is: 365
"""
