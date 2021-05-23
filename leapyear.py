def is_leapyear(year):
    byFour = int(year % 4)
    if byFour == 0:
        by100 = int(year % 100)
        if by100 == 0:
            by400 = int(year % 400)
            if by400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#year = int(input("enter year: "))
#print(is_leapyear(year))
