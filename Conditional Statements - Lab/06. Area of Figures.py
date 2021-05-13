import  math
figure = input()

if figure == "square":
   side= float(input())
   area = side * side
   print(f"{area:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    rad = float(input())
    area = math.pi * math.pow(rad, 2)
    print(f"{area:.3f}")
elif figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b / 2
    print(f"{area:.3f}")