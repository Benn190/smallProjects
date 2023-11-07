# program to calculate the number of days between any two dates in DDMMYYYY format

date1 = input("Choose a date...")
date1 = str(date1)
date2 = input("Choose another date...")
date2 = str(date2)

year1 = date1[4:]
year1 = int(year1)
year2 = date2[4:]
year2 = int(year2)

if year1 > year2:
    dateN = date1
    date1 = date2
    date2 = dateN
    year1 = date1[4:]
    year1 = int(year1)
    year2 = date2[4:]
    year2 = int(year2)