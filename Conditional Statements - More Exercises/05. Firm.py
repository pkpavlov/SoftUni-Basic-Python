import math
needed_hours = int(input())
days_for_project = int(input())
workers_overtime = int(input())

training = days_for_project - days_for_project * 0.1
work_time = training * 8
overtime = workers_overtime * (2 * days_for_project)
total_time = work_time + overtime

if total_time >= needed_hours:
    total_time = total_time - needed_hours
    print(f"Yes!{math.floor(total_time)} hours left.")
else:
    total_time = needed_hours - total_time
    print(f"Not enough time!{math.ceil(total_time)} hours needed.")