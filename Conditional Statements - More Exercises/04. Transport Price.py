kilometers = int(input())
part_of_the_day = input()

if kilometers < 20:
    if part_of_the_day == "day":
        price = 0.7 + kilometers * 0.79
        print(f"{price:.2f}")
    else :
        price = 0.7 + kilometers * 0.9
        print(f"{price:.2f}")
elif 20 <= kilometers <100:
    price = kilometers * 0.09
    print(f"{price:.2f}")
else:
    price = kilometers * 0.06
    print(f"{price:.2f}")