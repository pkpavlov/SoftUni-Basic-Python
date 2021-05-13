import math

number_magnolias = int(input()) * 3.25
number_hyacinths = int(input()) * 4
number_roses = int(input()) * 3.5
number_cacti = int(input()) * 8
gift_price = float(input())

benefit = number_magnolias + number_hyacinths + number_roses + number_cacti
benefit_after_tax = benefit * 0.95

if benefit_after_tax >= gift_price:
    left_money = benefit_after_tax - gift_price
    print(f"She is left with {math.floor(left_money)} leva.")
else:
    needed_money = gift_price - benefit_after_tax
    print(f"She will have to borrow {math.ceil(needed_money)} leva.")