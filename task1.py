year = int(input())

def is_year_leap(a):
    if a % 4 == 0 and a % 100 != 0:
        print("True")
    elif a % 400 == 0:
        print("True")

    else:
        print("False")

is_year_leap(year)
    
