"""
Simple Python Utility - Temperature Converter
Author: Wiem
Description:
A clean and beginner-friendly example project that converts
temperatures between Celsius and Fahrenheit.
"""

def c_to_f(celsius: float) -> float:
"""Convert Celsius to Fahrenheit."""
return (celsius * 9/5) + 32

def f_to_c(fahrenheit: float) -> float:
"""Convert Fahrenheit to Celsius."""
return (fahrenheit - 32) * 5/9

def main():
print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

```
choice = input("Choose option (1 or 2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {c_to_f(c):.2f}°F")

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F = {f_to_c(f):.2f}°C")

else:
    print("Invalid option. Please enter 1 or 2.")
```

if **name** == "**main**":
main()
