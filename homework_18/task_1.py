WEEK_DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print()

def get_daily_max_min_avg_temps(all_temperatures, index):
    min_temp_during_day = min(all_temperatures[index][0], all_temperatures[index][1], all_temperatures[index][2])
    max_temp_during_day = max(all_temperatures[index][0], all_temperatures[index][1], all_temperatures[index][2])
    average_daily_temp = (all_temperatures[index][0] + all_temperatures[index][1] + all_temperatures[index][2]) / 3
    
    return min_temp_during_day, max_temp_during_day, round(average_daily_temp, 2)

def get_temperature_details(all_temperatures):
    sum_of_temps = 0
    for day in range(7):
        morning_temperature = all_temperatures[day][0]
        afternoon_temperature = all_temperatures[day][1]
        evening_temperatue = all_temperatures[day][2]
        min_temp, max_temp, avg_daily_temp = get_daily_max_min_avg_temps(all_temperatures, day)
        sum_of_temps += avg_daily_temp
        
        print(f"{WEEK_DAYS[day]} temperatures during the day:")
        print(f"    Morning temperature - {morning_temperature}c")
        print(f"    Afternoon temperature - {afternoon_temperature}c")
        print(f"    Evening temperature - {evening_temperatue}c")
        print(f"    Minimum temperature during a day - {min_temp}c")
        print(f"    Maximum temperature during a day - {max_temp}c")
        print(f"    Average temperature during a day - {avg_daily_temp}c\n")
        
    return round(sum_of_temps / 7, 2)

def main():
    week_temperatures = ((33, 34, 28), (24, 31, 27), (24, 23, 27), \
           (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28)) 
    
    avg_week_temp = get_temperature_details(week_temperatures)
    print(f"Average temperature during the week - {avg_week_temp}c\n")

if __name__ == "__main__":
    main()
