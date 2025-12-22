name = input("What is your name? ")
age = int(input("What is your age? "))
faveNum = int(input("What is your favourite number? "))
fiveYears = age + 5
tenYears = age + 10
twentyYears = age + 20
faveNumDouble = faveNum * 2
faveNumByTen = faveNum * 10

print("=== About Me ===")
print(f"Name: {name}")
print(f"Current Age: {age}")
print(f"Favourite Number: {faveNum}")

print("=== Age Calculator ===")
print(f"In 5 years, I'll be: {fiveYears}")
print(f"In 10 years, I'll be: {tenYears}")
print(f"In 20 years, I'll be: {twentyYears}")

print("=== Number Fun ===")
print(f"My favourite number doubled: {faveNumDouble}")
print(f"My favourite number times 10: {faveNumByTen}")
