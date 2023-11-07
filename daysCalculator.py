# program to calculate the number of days between any two dates in DDMMYYYY format

date1 = input("Choose a date in DDMMYYYY format...")
date1 = str(date1)
date2 = input("Choose another date in DDMMYYYY format...")
date2 = str(date2)

# gets both inputted years as integers 
year1 = date1[4:]
year1 = int(year1)
year2 = date2[4:]
year2 = int(year2)

#swaps years if second inputted year comes first chronologically
if year1 > year2:
    dateN = date1
    date1 = date2
    date2 = dateN
    year1 = date1[4:]
    year1 = int(year1)
    year2 = date2[4:]
    year2 = int(year2)
    
day1 = date1[0:2]
day2 = date2[0:2]
month1 = date1[2:4]
month2 = date2[2:4]

day1 = int(day1)
day2 = int(day2)
month1 = int(month1)
month2 = int(month2)

daysUntil = 0

def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    else:
        return False
        

    return true

def daysLeftInMonth(year, month, days):
    if month == 1:
        daysUntil = 31 - days
    elif month == 2 and year:
        daysUntil = 31 - days