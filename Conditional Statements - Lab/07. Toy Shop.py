price_vacantion = float(input())
quantity_puzzle = int(input())
quantity_dolls = int(input())
quantity_teddy_bears = int(input())
quantity_minions = int(input())
quantity_trucks = int(input())

price_puzzle = 2.6
price_dolls = 3
price_teddy_bears = 4.1
price_minions = 8.2
price_trucks = 2

total_toys = quantity_puzzle + quantity_dolls + quantity_teddy_bears + quantity_minions + quantity_trucks
total_price_toys = quantity_puzzle * price_puzzle + quantity_dolls * price_dolls + quantity_teddy_bears * price_teddy_bears + \
                       quantity_minions * price_minions + quantity_trucks * price_trucks
if total_toys >= 50:
    discount = total_price_toys * 0.25
    price_after_discount = total_price_toys - discount
    rent = price_after_discount * 0.1
    profit = price_after_discount - rent
    if profit >= price_vacantion:
        left_money = profit - price_vacantion
        print(f"Yes! {left_money:.2f} lv left.")
    elif profit < price_vacantion:
        needed_money = price_vacantion - profit
        print(f"Not enough money! {needed_money:.2f} lv needed.")
elif total_toys < 50:
    rent = total_price_toys * 0.1
    profit = total_price_toys - rent
    if profit >=price_vacantion:
        left_money = profit - price_vacantion
        print(f"Yes! {left_money:.2f} lv left.")
    elif profit < price_vacantion:
        needed_money = price_vacantion - profit
        print(f"Not enough money! {needed_money:.2f} lv needed.")