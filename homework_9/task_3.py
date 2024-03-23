full_date = input('Input: ')

date, time = full_date.split('T')   # First var is assigned as whats on the left of the 'T' 
time, timezone = time.split('+')    # Same here

year, month, day = date.split('-')  # Example  2024-03-23 -> year-month-day -> year month day
mod_date = f"{day}-{month}-{year}"  # -> mod_date = 'day-month-year' In this instance 23-03-2024

hour, minute, second = time.split(':')  # Example  21:16:45 -> hour-minute-second
mod_hour = int(hour) - 12 if int(hour) >= 12 else hour
full_time = f"{mod_hour}:{minute}:{second}"  # -> mod_time = 9:16:45   {hour - 12} to get hours 1-12
full_time_divided = full_time.split('.')
mod_time = full_time_divided[0]


timezone = timezone.split(':')
mod_timezone = f"+{timezone[0]}"
mod_timezone = mod_timezone.replace('0', '', 1) if '0' in mod_timezone else mod_timezone

mod_full_date = f"{mod_date} {mod_time} {mod_timezone}"

print("Output:", mod_full_date)
