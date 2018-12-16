def is_leap(year):
    if year%100==0:
        if year%400==0:
            return True
        elif year%400!=0:
            return False
    else:
        if year%4==0:
            return True
        else:
            return False

year = int(raw_input())
if year>1900 and year<100000:
    print is_leap(year)
else:
    print ("limit exceeded")
