number = float(input())
input_unit = input()
output_unit = input()

if input_unit == "m" and output_unit == "cm":
    number = number * 100
    print(f"{number:.3f}")
elif input_unit == "m" and output_unit == "mm":
    number = number * 1000
    print(f"{number:.3f}")
elif input_unit == "cm" and output_unit == "m":
    number = number / 100
    print(f"{number:.3f}")
elif input_unit == "cm" and  output_unit == "mm":
    number = number / 0.1
    print(f"{number:.3f}")
elif input_unit == "mm" and  output_unit == "cm":
    number = number / 10
    print(f"{number:.3f}")
elif input_unit == "mm" and  output_unit == "m":
    number = number / 1000
    print(f"{number:.3f}")