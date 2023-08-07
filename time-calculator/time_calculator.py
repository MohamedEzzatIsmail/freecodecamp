def add_time(start, duration, day=False):

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sday = "same day"
    #start
    start_time = start.split()
    s_time = start_time[0].split(":")
    end = start_time[1]

    #duration
    duration_time = duration.split(":")

    if end == "PM":
        hour = int(s_time[0]) + 12
        s_time[0] = str(hour)

    new_hour = int(s_time[0])+int(duration_time[0])
    new_min = int(s_time[1])+int(duration_time[1])

    if new_min >= 60:
        hours = new_min // 60
        new_min -= hours * 60
        new_hour += hours

    days = 0
    if new_hour >= 24:
        days = new_hour // 24
        new_hour -= days * 24

    if new_hour > 0 and new_hour < 12:
        end = "AM"
    elif new_hour == 12:
        end = "PM"
    elif new_hour > 12:
        end = "PM"
        new_hour -= 12
    else:  # new_hour == 0
        end = "AM"
        new_hour += 12

    if days > 0:
        if days == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(days) + " days later)"
    else:
        days_later = ""

    if day:
        weeks = days // 7
        i = week.index(day.lower().capitalize()) + (days - 7 * weeks)
        if i > 6:
            i -= 7
        day = ", " + week[i]
    else:
        day = ""

    new_time = str(new_hour) + ":" + \
               (str(new_min) if new_min > 9 else ("0" + str(new_min))) + \
               " " + end + day + days_later

    return new_time
