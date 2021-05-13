fuel = input()
fuel_liters = float(input())
discount_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93
gasoline_discount = gasoline - 0.18
diesel_discount = diesel - 0.12
gas_discount = gas - 0.08
#################################### GASOLINE ################################
if fuel == "Gasoline":
    if discount_card == "Yes":
        if 20.00 <=fuel_liters <= 25.00:
            price_fuel = fuel_liters * gasoline_discount * 0.92
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters > 25.00:
            price_fuel = fuel_liters * gasoline_discount * 0.9
            print(f"{price_fuel:.02f} lv.")
        else:
            price_fuel = fuel_liters * gasoline_discount
            print(f"{price_fuel:.02f} lv.")
    else:
        if 20.00 <= fuel_liters <= 25.00:
            price_fuel = fuel_liters * gasoline * 0.92
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters > 25.00:
            price_fuel = fuel_liters * gasoline * 0.9
            print(f"{price_fuel:.02f} lv.")
        else:
            price_fuel = fuel_liters * gasoline
            print(f"{price_fuel:.02f} lv.")
#################################### DIESEL ################################
elif fuel == "Diesel":
    if discount_card == "Yes":
        if 20.00 <=fuel_liters <= 25.00:
            price_fuel = fuel_liters * diesel_discount * 0.92
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters > 25.00:
            price_fuel = fuel_liters * diesel_discount * 0.9
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters < 20:
            price_fuel = fuel_liters * diesel_discount
            print(f"{price_fuel:.02f} lv.")
    elif discount_card == "No":
        if 20.00 <= fuel_liters <= 25.00:
            price_fuel = fuel_liters * diesel * 0.92
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters < 20.00:
            price_fuel = fuel_liters * diesel
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters > 25.00:
            price_fuel = fuel_liters * diesel * 0.9
            print(f"{price_fuel:.02f} lv.")

#################################### GAS ################################
elif fuel == "Gas":
    if discount_card == "Yes":
        if 20.00 <=fuel_liters <= 25.00:
            price_fuel = fuel_liters * gas_discount * 0.92
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters > 25.00:
            price_fuel = fuel_liters * gas_discount * 0.9
            print(f"{price_fuel:.02f} lv.")
        else:
            price_fuel = fuel_liters * gas_discount
            print(f"{price_fuel:.02f} lv.")
    else:
        if 20.00 <= fuel_liters <= 25.00:
            price_fuel = fuel_liters * gas * 0.92
            print(f"{price_fuel:.02f} lv.")
        elif fuel_liters > 25.00:
            price_fuel = fuel_liters * gas * 0.9
            print(f"{price_fuel:.02f} lv.")
        else:
            price_fuel = fuel_liters * gas
            print(f"{price_fuel:.02f} lv.")