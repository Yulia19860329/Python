number = input("positive_integer")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print("The biggest number", x)
