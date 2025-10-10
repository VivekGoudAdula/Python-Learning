# IF-ELSE STATEMENTS

a = 33
b = 12

# ----------------------------------

# IF STATEMENT
if a>b:
    print("a is greater than b")

# ----------------------------------

# IF-ELSE STATEMENT
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# ----------------------------------

# IF-ELIF-ELSE STATEMENT
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")

# ----------------------------------

# SHORT HAND IF
if a<b: print("a is less than b")

# ----------------------------------

# SHORT HAND IF-ELSE
print("A is greater") if a>b else print("B is greater")

# ----------------------------------

# AND & OR
if a>10 and b<10:
    print("Both conditions are True")

if a == 10 or a>10:
    print("At least one condition is True")

# ----------------------------------

# NESTED IF
if a>b:
    if a>30:
        if a<40:
            print("a lies between 30 and 40")

# ----------------------------------

# NOT
if not a==b:
    print("a is not equal to b")

# ----------------------------------

# PASS STATEMENT
if a!=40:
    pass # Used to avoid errors when no code is to be executed

# ----------------------------------

# MATCH-CASE (Python 3.10+)
month = 5
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case default:
        print("Other day")

# COMBINE CASES
match day:
    case 1 | 2| 3| 4| 5| 6:
        print("Weekday")
    case 7:
        print("Holiday")
    case _:
        print("Other day")

# IF-STATEMENTS AS GUARDS
match day:
    case 1|2|3|4|5 if month == 5:
        print("May Month")
    case 1|2|3|4|5 if day == 3:
        print("3rd Day")

# ----------------------------------