# simple_interest.py
# Program to calculate Simple Interest

import sys

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest given principal, rate, and time.
    """
    return (principal * rate * time) / 100


if __name__ == "__main__":
    print("=== Simple Interest Calculator ===")

    
        # Case 1: Arguments passed (for Jenkins or CLI)
    if len(sys.argv) == 4:
        p = float(sys.argv[1])
        r = float(sys.argv[2])
        t = float(sys.argv[3])

        # Case 2: No arguments passed (console use)
    else:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the rate of interest (%): "))
        t = float(input("Enter the time (in years): "))

    print("\n--- Program Parameters ---")
    print(f"Principal: {p}")
    print(f"Rate: {r}")
    print(f"Time: {t}")

    si = calculate_simple_interest(p, r, t)

    print("\n--- Result ---")
    print(f"Simple Interest: {si}")

   