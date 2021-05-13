day_off = int(input())

work_day = 365 - day_off
time_for_paly = work_day * 63 + day_off * 127

if time_for_paly > 30000:
    diff = time_for_paly - 30000
    diff_h = diff // 60
    diff_m = diff % 60
    print("Tom will run away")
    print(f"{diff_h} hours and {diff_m} minutes more for play")
elif time_for_paly < 30000:
    diff = 30000 - time_for_paly
    diff_h = diff // 60
    diff_m = diff % 60
    print("Tom sleeps well")
    print(f"{diff_h} hours and {diff_m} minutes less for play")
