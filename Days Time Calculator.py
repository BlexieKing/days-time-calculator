go = "yes"
while go == "yes":
    print("")
    print("Days time calculator")
    print("")
    print("What is the date today? xx/xx/xxxx")
    date = input(": ")
    dates = date.split("/")
    while dates[0].isdigit()==False or dates[1].isdigit()==False or dates[2].isdigit() == False:
        print("Please enter a valid date!")
        date = input(": ")
        dates = date.split("/")
    print("How many days time do you want to work out?")
    daystime = input(": ")
    daystimet = daystime
    while daystime.isdigit() == False:
        print("Please enter a valid amount of days!")
        daystime = input(": ")
    daystime = int(daystime)
    daystimet = daystime
    yrt = "year"
    if int(dates[2])%4 == 0:
        yrt = "leapyear"
    if yrt == "year":
        jan = 31
        feb = 28
        mar = 31
        apr = 30
        may = 31
        jun = 30
        jul = 31
        aug = 31
        sep = 30
        octo = 31
        nov = 30
        dec = 31
        jand = 31
        febd = 28
        mard = 31
        aprd = 30
        mayd = 31
        jund = 30
        juld = 31
        augd = 31
        sepd = 30
        octod = 31
        novd = 30
        decd = 31
    else:
        jan = 31
        feb = 29
        mar = 31
        apr = 30
        may = 31
        jun = 30
        jul = 31
        aug = 31
        sep = 30
        octo = 31
        nov = 30
        dec = 31
        jand = 31
        febd = 29
        mard = 31
        aprd = 30
        mayd = 31
        jund = 30
        juld = 31
        augd = 31
        sepd = 30
        octod = 31
        novd = 30
        decd = 31
    month = int(dates[1])
    days = int(dates[0])
    year = int(dates[2])
    if month == 1:
        daysleft = jan
    elif month == 2:
        daysleft = feb
    elif month == 3:
        daysleft = mar
    elif month == 4:
        daysleft = apr
    elif month == 5:
        daysleft = may
    elif month == 6:
        daysleft = jun
    elif month == 7:
        daysleft = jul
    elif month == 8:
        daysleft = aug
    elif month == 9:
        daysleft = sep
    elif month == 10:
        daysleft = octo
    elif month == 11:
        daysleft = nov
    elif month == 12:
        daysleft = dec
    else:
        month = 1
        daysleft = jan
    daysleft = days
    while daystime > 0:
        daystime = daystime-1
        if month == 1:
            daysleft = daysleft+1
            days = days+1
            monthd = jand
        elif month == 2:
            daysleft = daysleft+1
            days = days+1
            monthd = febd
        elif month == 3:
            days = days+1
            daysleft = daysleft+1
            monthd = mard
        elif month == 4:
            days = days+1
            daysleft = daysleft+1
            monthd = aprd
        elif month == 5:
            days = days+1
            daysleft = daysleft+1
            monthd = mayd
        elif month == 6:
            days = days+1
            daysleft = daysleft+1
            monthd = jund
        elif month == 7:
            days = days+1
            daysleft = daysleft+1
            monthd = juld
        elif month == 8:
            aug=aug-1
            daysleft = daysleft+1
            monthd = augd
        elif month == 9:
            sep=sep-1
            daysleft = daysleft+1
            monthd = sepd
        elif month == 10:
            octo=octo-1
            daysleft = daysleft+1
            monthd = octod
        elif month == 11:
            nov=nov-1
            daysleft = daysleft+1
            monthd = novd
        elif month == 12:
            dec=dec-1
            daysleft = daysleft+1
            monthd = decd
        if daysleft == (monthd+1):
            if month == 12:
                year = year + 1
                month = 1
                if month == 1:
                    daysleft = jand
                elif month == 2:
                    daysleft = febd
                elif month == 3:
                    daysleft = mard
                elif month == 4:
                    daysleft = aprd
                elif month == 5:
                    daysleft = mayd
                elif month == 6:
                    daysleft = jund
                elif month == 7:
                    daysleft = juld
                elif month == 8:
                    daysleft = augd
                elif month == 9:
                    daysleft = sepd
                elif month == 10:
                    daysleft = octod
                elif month == 11:
                    daysleft = novd
                elif month == 12:
                    daysleft = decd
            else:
                month = month + 1
                daysleft=1
    print("")
    if days < 10:
        dayst = "0" + str(daysleft)
    print("The date after " + str(daystimet) + " days is " + str(daysleft) + "/" + str(month) + "/" + str(year) + "!")
    print("")
    print("Again? 'y' or 'n'")
    answer = input(": ")
    if answer == "n":
        go = "no"
        print("Bye bye.")
    elif answer == "y":
        print("")
    else:
        print("You gave an invalid answer... So I'll start anyway!")
        print("")
