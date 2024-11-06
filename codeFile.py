# CLI-based Unit Converter in Python

def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371
    }
    # Convert from the original unit to meters, then to the target unit
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value  # if from_unit == to_unit

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length Conversion (meters, kilometers, miles)")
        print("2. Weight Conversion (grams, kilograms, pounds)")
        print("3. Temperature Conversion (Celsius, Fahrenheit, Kelvin)")
        print("4. Exit")
        
        choice = input("Choose a conversion type: ")
        
        if choice == '1':
            value = float(input("Enter value: "))
            from_unit = input("Convert from (meters/kilometers/miles): ").lower()
            to_unit = input("Convert to (meters/kilometers/miles): ").lower()
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is {result} {to_unit}")
            
        elif choice == '2':
            value = float(input("Enter value: "))
            from_unit = input("Convert from (grams/kilograms/pounds): ").lower()
            to_unit = input("Convert to (grams/kilograms/pounds): ").lower()
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} is {result} {to_unit}")
            
        elif choice == '3':
            value = float(input("Enter temperature: "))
            from_unit = input("Convert from (celsius/fahrenheit/kelvin): ").lower()
            to_unit = input("Convert to (celsius/fahrenheit/kelvin): ").lower()
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value}° {from_unit.capitalize()} is {result}° {to_unit.capitalize()}")
            
        elif choice == '4':
            print("Exiting Unit Converter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
