leap_year=int(input("enter the number = "))
if leap_year%4==0:
    if leap_year%100:
        if leap_year%400:
            print("century")
        else:
            print("no")
    else:
        print("leap_year")
else:
    print("nothing")