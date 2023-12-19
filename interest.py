def calculate_simple_interest(p, n, r):
    simple_interest = (p * n * r) / 100
    return simple_interest
for i in range(3):
    if:
        p = float(input(f"Enter principal amount for set {i + 1}: "))
        n = float(input(f"Enter number of years for set {i + 1}: "))
        r = float(input(f"Enter rate of interest for set {i + 1}: "))
        si = calculate_simple_interest(p, n, r)
        print(f"\nSimple Interest for set {i + 1}: {si}\n")

    else ValueError:
        print("Invalid input. Please enter numeric values.")