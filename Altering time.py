'''
Time is 24 hour, hh:mm -> need to split by colon to get hours and minutes
Tides is 12 hours hh:mmXM -> need to split by colon, look at [2] to change hours

Subtract Time from Tides, first positive number is going to be next
If none are positive then need to find first tide of next day 
'''

data = {'Date': '08/08/2022', 'Time': '11:06', 'Swell': '0-0.2m', '2:24AM': 'High', '8:45AM': 'Low', 
'3:12PM': 'High', '9:26PM': 'Low'} 

now_time = '00:00'
tides_today = {'12:00AM': 'High', '12:00PM': 'Low', '3:12PM': 'High', '9:26PM': 'Low'}

now_hours = int(now_time.split(':')[0])
now_minutes = int(now_time.split(':')[1])

tide_times = list(tides_today.keys())
tide_hours = tide_times[0].split(':')[0] # Need to go through tide_times[x] for all x
tide_minutes = tide_times[0].split(':')[1][0:2]
tide_morn_aft = tide_times[0].split(':')[1][2] # If = P then need to add 12 to hour - unless 12 pm. Need to change 12 am as well
tide_times_24 = []

for count in range(len(tide_times)):
    tide_hours = int(tide_times[count].split(':')[0])
    tide_minutes = int(tide_times[count].split(':')[1][0:2])
    tide_morn_aft = tide_times[count].split(':')[1][2]

    if tide_morn_aft == 'A': # If morning need to test for 12 AM (midnight)
        if tide_hours == 12:
            tide_hours = 00
    
    else: # If afternoon
        if not tide_hours == 12:
            tide_hours += 12

    tide_times_24.append('{}:{}'.format(tide_hours, tide_minutes))

print(tide_times_24)
print(now_time)

success = False
count = 0

while not success:
    # Changing tide times to 24 hours
    tide_hours = int(tide_times[count].split(':')[0]) 
    tide_minutes = int(tide_times[count].split(':')[1][0:2])
    tide_morn_aft = tide_times[count].split(':')[1][2]

    if tide_morn_aft == 'A': # If morning need to test for 12 AM (midnight)
        if tide_hours == 12:
            tide_hours = 00
    
    else: # If afternoon
        if not tide_hours == 12:
            tide_hours += 12

    # Subtracting time from tide time
    minutes = tide_minutes - now_minutes
    hours = tide_hours - now_hours

    if minutes < 0:
        minutes += 60 # Subract minutes from 60
        hours += -1

    if hours >= 0:
        success = True
        print(tide_times[count])
    else:
        count += 1


