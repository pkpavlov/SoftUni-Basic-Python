import math
world_record_sec = float(input())
distance_in_meters = float(input())
time_in_sec_for_one_meter = float(input())

ivan_times = distance_in_meters * time_in_sec_for_one_meter
delay =math.floor(distance_in_meters / 15) * 12.5
ivan_total_times = ivan_times + delay

if ivan_total_times >= world_record_sec:
    needed_second = ivan_total_times - world_record_sec
    print(f"No, he failed! He was {needed_second:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {ivan_total_times:.2f} seconds.")