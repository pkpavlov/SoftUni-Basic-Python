import math
day_left = int(input())
left_food_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_gr = float(input()) / 1000

total_food_kg = food_for_dog_kg + food_for_cat_kg + food_for_turtle_gr
food_for_left_day = total_food_kg * day_left

if left_food_kg >= food_for_left_day:
    left_food = left_food_kg - food_for_left_day
    print(f"{math.floor(left_food)} kilos of food left.")
else:
    needed_food =  food_for_left_day - left_food_kg
    print(f"{math.ceil(needed_food)} more kilos of food are needed.")

