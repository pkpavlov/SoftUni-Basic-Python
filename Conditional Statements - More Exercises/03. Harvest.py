import math
area_vineyard = int(input()) #X
grapes = float(input()) #Y
needed_liters_wine = int(input())  #Z
number_workers = int(input())

total_grapes = area_vineyard * grapes *0.4

wine = total_grapes / 2.5

if wine >= needed_liters_wine:
    left_wine = wine - needed_liters_wine
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    for_one_person = left_wine / number_workers
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(for_one_person)} liters per person.")
else:
    needed_wine = needed_liters_wine - wine
    print(f"It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.")
