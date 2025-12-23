print("Welcome to the Restaurant Receipt Generator!")

name = input("What is your name? ")
server = input("What is the name of your server? ")
restaurant = input("What is the name of the Restaurant? ")
app = float(input("How much was the appetizer? "))
main = float(input("How much was the main? "))
dessert = float(input("How much was the dessert? "))
drink = float(input("How much was the drink? "))
sub1 = "Appetizer"
sub2 = "Main Course"
sub3 = "Dessert"
sub4 = "Drink"
sub5 = "Subtotal"
sub6 = "Tax (8%)"
sub7 = "Tip (18%)"
sub8 = "TOTAL"

subtotal = float(app + main + dessert + drink)
tax = 8
tip = 18
total_tax = float((subtotal * tax) / 100)
total_tip = float((subtotal * tip) / 100)
grand_total = subtotal + total_tax + total_tip

print("=" * 40)
print(f"{restaurant:^40}".upper())
print("=" * 40)
print("\n")

print("Server: " + server)
print("\n")

print("-" * 40)
print(("ITEMS"))
print("-" * 40)
print(f"{sub1:<30}${app:>6.2f}")
print(f"{sub2:<30}${main:>6.2f}")
print(f"{sub3:<30}${dessert:>6.2f}")
print(f"{sub4:<30}${drink:>6.2f}")
print("-" * 40)
print("\n")

print(f"{sub5:<30}${subtotal:>6.2f}")
print(f"{sub6:<30}${total_tax:>6.2f}")
print(f"{sub7:<30}${total_tip:>6.2f}")
print("-" * 40)
print(f"{sub8:<30}${grand_total:>6.2f}")
print("=" * 40)
