"""
1️⃣ Smart Temperature Converter
Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.
(Use explicit type conversion and arithmetic operators.)
 Formula:
Fahrenheit = (C × 9/5) + 32


Kelvin = C + 273.15


Example:
Enter temperature in Celsius: 25
Output:
Fahrenheit: 77.0
Kelvin: 298.15
"""

C = float(input("Enter temperature in Celsius: "))
print("Fahrenheit: ", (C * 9/5) + 32)
print("Kelvin: ", C + 273.15)

