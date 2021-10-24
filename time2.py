str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")               #fixed miss spelling
time = int(str_time)
wait_time = int(str_wait_time)                                              #fixed miss spelling

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
