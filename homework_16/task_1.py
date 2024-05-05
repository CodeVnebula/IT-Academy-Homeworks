temperature_list = [22, 25, 19, 23, 25, 26, 23]
def average_temperature() -> float:
    sum_ = 0
    for i in temperature_list:
        sum_ += i
    average_temp = sum_ / len(temperature_list)
    return average_temp

def main():
    avg_temperature = average_temperature()
    print(f"Average temperature of {temperature_list} temperatures is: {avg_temperature}")

if __name__ == "__main__":
    main()
