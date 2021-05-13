film_budget = float(input())
people = int(input())
dress_price_for_one_man = float(input())

decor = film_budget * 0.1
price_for_all_people = people * dress_price_for_one_man
price_for_all_people_after_discont = price_for_all_people - (price_for_all_people * 0.1)
total_film_price = decor + price_for_all_people
total_film_price_whit_discount = decor + price_for_all_people_after_discont
if 1.00 <= film_budget <= 1000000.00 and 1 <= people <= 500 and 1.00 <= dress_price_for_one_man <= 1000.00:
    if people > 150:
        if total_film_price_whit_discount > film_budget:
            needed_money = total_film_price_whit_discount - film_budget
            print("Not enough money!")
            print(f"Wingard needs {needed_money:.2f} leva more.")
        elif total_film_price_whit_discount <= film_budget:
            money_left = film_budget - total_film_price_whit_discount
            print("Action!")
            print(f"Wingard starts filming with {money_left:.2f} leva left.")
    elif people < 150:
        if total_film_price > film_budget:
            needed_money = total_film_price - film_budget
            print("Not enough money!")
            print(f"Wingard needs {needed_money:.2f} leva more.")
        elif total_film_price <= film_budget:
            money_left = film_budget - total_film_price
            print("Action!")
            print(f"Wingard starts filming with {money_left:.2f} leva left.")
