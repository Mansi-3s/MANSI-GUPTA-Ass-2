name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
if age > 18:
    print(f"Hello {name}, you are eligible to vote in {city}.")
else:
    print(f"Sorry {name}, you are too young.")