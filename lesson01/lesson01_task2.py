seconds = int(input("Enter time in seconds"))
difference = seconds % 3600
hour = seconds//3600
hour_difference = seconds % 3600
minute = difference//60
sec = difference % 60
print(f"Time is {hour}:{minute}:{sec}")


