'''
Time is 24 hour, hh:mm -> need to split by colon to get hours and minutes
Tides is 12 hours hh:mmXM -> need to split by colon, look at [2] to change hours

Subtract Time from Tides, first positive number is going to be next
If none are positive then need to find first tide of next day 
'''

### MADE UP DATA - WILL BE READ FROM CSV

now_time = '21:27'
tides_today = {'2:24AM': 'High', '8:45AM': 'Low', '3:12PM': 'High', '9:26PM': 'Low'}


### START OF CODE

now_hours = int(now_time.split(':')[0])
now_minutes = int(now_time.split(':')[1])

tide_times = list(tides_today.keys())
tide_times_24 = []
end_of_day = True                                               # Will change to False if an early tide is found

for count, time in enumerate(tide_times):

### CONVERTING TO 24 HOUR

    tide_hours = int(tide_times[count].split(':')[0])           # Hours found infront of colon
    tide_minutes = int(tide_times[count].split(':')[1][0:2])    # Minutes found after colon
    tide_morn_aft = tide_times[count].split(':')[1][2]          # AM/PM determined by letter after minutes

    if tide_morn_aft == 'A':                                     # If morning need to test for 12 AM (midnight)
        if tide_hours == 12: 
            tide_hours = 00
    
    else:                                                       # If afternoon
        if not tide_hours == 12:                                # Need to convert afternoon hours to 24 hour by adding 12
            tide_hours += 12

### SUBTRACTING FROM TIME NOW

    minutes = tide_minutes - now_minutes
    hours = tide_hours - now_hours

    if minutes < 0:                                             # If minutes have gone negative (need to take an hour off)
        minutes += 60                                           # Subract minutes from 60
        hours += -1                                             # Take an hour off

    if hours >= 0:        

        if count == 0:                                          # If before first tide of the day
            now_minutes_since_midnight = 60 * now_hours + now_minutes
            minutes_to_midnight = 1440 - (60 * (tide_hours - 6 + 24) + tide_minutes)

            fraction_through_tide = (minutes_to_midnight + now_minutes_since_midnight)/360
            end_of_day = False
            break
            
        else:
            minutes_next_tide = 60 * tide_hours + tide_minutes
            previous_hours = int(tide_times[count - 1].split(':')[0])
            previous_minutes = int(tide_times[count - 1].split(':')[1][0:2])
            minutes_previous_tide = 60 * previous_hours + previous_minutes

            tide_length = minutes_next_tide - minutes_previous_tide

            fraction_through_tide = (tide_length - (60 * hours + minutes))/ (tide_length)
            end_of_day = False
            break


if not end_of_day:
    tide_type = tides_today.get(tide_times[count])
    print('The time until the next {} tide is {} hours and {} minutes'.format(tide_type, hours, minutes))

else:
    tide_type = tides_today.get(tide_times[count - 1])
    print('The next tide is tomorrow it will be {}'.format(tide_type))

    total_now_minutes = 60 * now_hours + now_minutes
    minutes_previous_tide = 60 * tide_hours + tide_minutes

    fraction_through_tide = (total_now_minutes - minutes_previous_tide)/ 360

print("It is {} % through the tide".format(fraction_through_tide * 100))
