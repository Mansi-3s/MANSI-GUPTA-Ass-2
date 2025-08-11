
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
common = a & b
if common > 0 and a > b:
    print("✅ a and b share some bits AND a is greater than b.")
elif common == 0 or b > a:
    print("⚠️ No common bits OR b is greater than a.")
else:
    print("ℹ️ Some other condition met.")
