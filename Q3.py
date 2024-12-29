print("Season code")
print("Autumn   1")
print("Winter   2")
print("Spring   3")
print("Summer   4")

sc = int(input("Enter your Season code: "))

if sc == 1:
    print("Autumn")
elif sc == 2:
    print("Winter")
elif sc == 3:
    print("Spring")
elif sc == 4:
    print("Summer")
else:
    print("Invalid code")


if sc == 1:
    season = "Autumn"
else:
    if sc == 2:
        season = "Winter"
    else:
        if sc == 3:
            season = "Spring"
        else:
            if sc == 4:
                season = "Summer"
            else:
                season = "Invalid code"

print(season)
