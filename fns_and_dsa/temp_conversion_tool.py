FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return(celcius)

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * (celsius +32)
    return(fahrenheit)

temp_input = input("Enter the temperature to convert: ")
temperature = float(temp_input)

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == 'C':
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
elif unit == 'F':
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celsius}°C")
else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
