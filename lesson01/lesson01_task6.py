a = float(input("Enter first day:"))
b = float(input("Enter last day:"))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
print(day)