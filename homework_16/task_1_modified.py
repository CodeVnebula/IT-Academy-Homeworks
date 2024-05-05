temperature_list = [22, 25, 19, 23, 25, 26, 23]
def average_temperature() -> float:
    return sum(temperature_list) / len(temperature_list)
     
def main():
    avg_temperature = average_temperature()
    print(f"Average temperature of {temperature_list} temperatures is: {avg_temperature}")

if __name__ == "__main__":
    main()
