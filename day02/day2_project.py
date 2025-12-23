print("Welcome to the Restaurant Receipt Generator!")

# Get user input
name = input("What is your name? ")
server = input("What is the name of your server? ")
restaurant = input("What is the name of the Restaurant? ")
app = float(input("How much was the appetizer? "))
main = float(input("How much was the main? "))
dessert = float(input("How much was the dessert? "))
drink = float(input("How much was the drink? "))

# Constants
tax_rate = 0.08
tip_rate = 0.18

# Calculations
subtotal = app + main + dessert + drink
total_tax = subtotal * tax_rate
total_tip = subtotal * tip_rate
grand_total = subtotal + total_tax + total_tip

# Print receipt 
print("=" * 40)
print(f"{restaurant:^40}".upper())
print("=" * 40)
print()

print(f"Customer: {name}")
print(f"Server: {server}")
print()

print("-" * 40)
print(("ITEMS"))
print("-" * 40)
print(f"{'Appetizer':<30}${app:>6.2f}")
print(f"{'Main Course':<30}${main:>6.2f}")
print(f"{'Dessert':<30}${dessert:>6.2f}")
print(f"{'Drink':<30}${drink:>6.2f}")
print("-" * 40)
print()

print(f"{'Subtotal':<30}${subtotal:>6.2f}")
print(f"{'Tax (8%)':<30}${total_tax:>6.2f}")
print(f"{'Tip (18%)':<30}${total_tip:>6.2f}")
print("-" * 40)
print(f"{'TOTAL':<30}${grand_total:>6.2f}")
print("=" * 40)
print()
print("Thanks for dining with us!")
