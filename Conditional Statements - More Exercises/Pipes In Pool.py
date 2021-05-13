pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
hours_work_absent = float(input())

first_pipe_volume = first_pipe_flow * hours_work_absent
second_pipe_volume = second_pipe_flow * hours_work_absent

total_volume = first_pipe_volume + second_pipe_volume

pool_volume_percentage = (total_volume / pool_volume) * 100
first_pipe_percentage = first_pipe_volume /total_volume  * 100
second_pipe_percentage = second_pipe_volume /total_volume  * 100
overfill = total_volume - pool_volume

if total_volume <= pool_volume:
    print(f"The pool is {pool_volume_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.")
else:
    print(f"For {hours_work_absent} hours the pool overflows with {overfill:.2f} liters.")