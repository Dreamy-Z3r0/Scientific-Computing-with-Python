def add_time(start, duration, startDoW = None):
    # Holder to the next timestamp
    new_time = None

    ### Process the start timestamp and the elapsed time
    # Obtain the elapsed time by hours and minute
    delimiterIndex = duration.index(':')
    hours = int(duration[0:delimiterIndex])
    minutes = int(duration[delimiterIndex+1:])

    # Convert start to lower-case characters to process through case-insensitivity
    start = start.lower()

    # Obtain start time by hour and minute in 24H format
    if 'pm' == start[-2:]:
        startHour = start[0 : start.index(':')]
        hours += int(startHour) + 12  
    else:
        startHour = start[0 : start.index(':')]
        hours += int(startHour)

    # Obtain the minute part of the next timestamp
    minute = start[start.index(':') + 1 : start.index(' ')]
    minutes += int(minute)

    # Obtain the hour part of the next timestamp
    temp = minutes // 60
    hours += temp
    minutes -= temp * 60

    # Obtain the days after the elapsed time
    days = (hours // 24)
    hours -= (days * 24)

    ### Put the next timestamp to a string
    # Minute part
    new_time = str(minutes)
    if minutes < 10:
        new_time = ':0' + new_time
    else:
        new_time = ':' + new_time

    # Convert hour part into the 12H format; Add suitable AM/PM indicator
    if 0 == hours:
        hours = 12
        new_time += " AM"
    elif 12 == hours:
        new_time += " PM"
    elif hours > 12:
        hours -= 12
        new_time += " PM"
    else:
        new_time += " AM"

    # Add hour part to the timestamp string
    new_time = str(hours) + new_time

    # Add day of week if the corresponding input is specified
    if startDoW is not None:
        startDoW = startDoW.lower().capitalize()
        DoW = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']

        index = DoW.index(startDoW) + days
        index = index % 7

        new_time += ', ' + DoW[index]

    # Add the elapsed day period
    if 1 == days:
        new_time += ' (next day)'
    elif 1 < days:
        new_time += ' (' + str(days) + ' days later)'
    else:
        pass
    
    ### Return the future timestamp
    return new_time

if __name__ == "__main__":
    print(add_time('3:00 PM', '3:10'))
    # Returns: 6:10 PM

    print(add_time('11:30 AM', '2:32', 'Monday'))
    # Returns: 2:02 PM, Monday

    print(add_time('11:43 AM', '00:20'))
    # Returns: 12:03 PM

    print(add_time('10:10 PM', '3:30'))
    # Returns: 1:40 AM (next day)

    print(add_time('11:43 PM', '24:20', 'tueSday'))
    # Returns: 12:03 AM, Thursday (2 days later)

    print(add_time('6:30 PM', '205:12'))
    # Returns: 7:42 AM (9 days later)