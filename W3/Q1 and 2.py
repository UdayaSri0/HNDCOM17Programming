x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x > y:
    print("Max num",x)
    print("Min num",y)
else:
    print("Max num",y)
    print("Min num",x)


if x > y:
    h = x
    l = y
else:
    h = y
    l = x
    
print("Max num",h)
print("Min num",l)