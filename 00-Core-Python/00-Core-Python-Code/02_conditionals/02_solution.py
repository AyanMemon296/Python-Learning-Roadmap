age = int(input("Enter your age: "))

day = str(input("Enter the day of the week (Monday, Tuesday, etc.): "))

if age >=18:
    price = 12

else:
    price = 8

if day == "Wednesday":
    price = price - 2

print(f"The ticket price is: ${price}")