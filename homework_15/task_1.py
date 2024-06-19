def convert_temperature(temperature_unit: str, temperature: int):
    # C = (F - 32) * 5/9 , F = C * 9/5 + 32
    if temperature_unit == 'c':
        return temperature * 9 / 5 + 32
    return (temperature - 32) * 5 / 9


def main():
    while True:
        temp_unit = input("Enter temperature unit Celsius or Fahrenheit (c/f): ").lower()
        if temp_unit in ['c', 'f']:
            break

    if temp_unit == "c":
        temperature = int(input("Enter temperature in Celsius: "))
    else:
        temperature = int(input("Enter temperature in Fahrenheit: "))
    
    converted_temperature = convert_temperature(temp_unit, temperature)
    if temp_unit == 'c':
        print(f"{temperature}C = {converted_temperature}F")
    else:
        print(f"{temperature}F = {converted_temperature}C")

if __name__ == "__main__":
    main()
