'''
Time is 24 hour, hh:mm -> need to split by colon to get hours and minutes
Tides is 12 hours hh:mmXM -> need to split by colon, look at [2] to change hours

Subtract Time from Tides, first positive number is going to be next
If none are positive then need to find first tide of next day 
'''

data = {'Date': '08/08/2022', 'Time': '11:06', 'Swell': '0-0.2m', '2:24AM': 'High', '8:45AM': 'Low', 
'3:12PM': 'High', '9:26PM': 'Low'} 

now_time = '2:06'
tides_today = {'2:24AM': 'High', '8:45AM': 'Low', '3:12PM': 'High', '9:26PM': 'Low'}

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
start_of_day = False
end_of_day = False
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
        if count == 0: # If start of day then needs yesterday's data
            start_of_day = True

        success = True

    else:
        if count < len(tide_times) - 1:
            count += 1
        else:
            end_of_day = True # If end of day then needs tomorrow's data
            break

# Returning when next tide will be
if not end_of_day:
    tide_type = tides_today.get(tide_times[count])
    print('The time until the next {} tide is {} hours and {} minutes'.format(tide_type, hours, minutes))

else:
    print('The next tide will be tomorrow, need to update code...')

# Calculate percentage through tide, need to convert to minutes
minutes_through_tide = 60 * hours + minutes

minutes_next_tide = tide_hours * 60 + tide_minutes

if not end_of_day and not start_of_day:
    previous_hours = int(tide_times[count - 1].split(':')[0])
    previous_minutes = int(tide_times[count - 1].split(':')[1][0:2])
    minutes_previous_tide = 60 * previous_hours + previous_minutes

    fraction_through_tide = minutes_through_tide/ (minutes_next_tide - minutes_previous_tide)

    print("It is {} % through the tide".format(fraction_through_tide * 100))

else:
    print('It is the start or the end of the day, code needs to be updated...')
