#De Gironimo Matteo 5A


def get_hours_minutes_seconds(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return str(hour)+"h "+str(minutes)+"m "+str(seconds)+"s"
    

print(get_hours_minutes_seconds(30))
print(get_hours_minutes_seconds(60))
print(get_hours_minutes_seconds(90))
print(get_hours_minutes_seconds(3600))
print(get_hours_minutes_seconds(3601))
print(get_hours_minutes_seconds(3661))
print(get_hours_minutes_seconds(90042))
print(get_hours_minutes_seconds(0))