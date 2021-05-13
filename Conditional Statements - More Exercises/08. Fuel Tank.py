fuel = input()
liters_in = float(input())

if fuel == "Diesel":
    if liters_in >= 25:
        print("You have enough diesel.")
    else:
        print("Fill your tank with diesel!")
elif fuel == "Gasoline":
    if liters_in >= 25:
        print("You have enough gasoline.")
    else:
        print("Fill your tank with gasoline!")
elif fuel == "Gas":
    if liters_in >= 25:
        print("You have enough gas.")
    else:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")
