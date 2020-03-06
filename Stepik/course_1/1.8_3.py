X = int(input())
H = int(input())
M = int(input())

hours_to_minutes = H * 60
all_time_in_minutes = hours_to_minutes + M + X
alarm_hours = all_time_in_minutes // 60
alarm_minutes = all_time_in_minutes % 60
print(alarm_hours)
print(alarm_minutes)
