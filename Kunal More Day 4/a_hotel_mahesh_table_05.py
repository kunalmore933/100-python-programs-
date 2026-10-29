
width = 12
coffee_price = 25.00
sandwich_price = 30.00
total_price = coffee_price + sandwich_price

total_width = width + 8
print(f"{'HOTEL MAHESH':^{total_width}}")
print("\n" * 1, end="")

print(f"{'Item':<{width}}{'Price':>8}")
print("-" * (width + 8))
print(f"{'Coffee':<{width}}{25.00:>8.2f}")
print(f"{'Sandwich':<{width}}{30.00:>8.2f}")
print("\n" * 3, end="")
print(f"{'Total':<{width}}{total_price:>8.2f}")
      




