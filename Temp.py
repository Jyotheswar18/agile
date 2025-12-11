# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    conversions = {
        '1': ("Enter Celsius: ", "°C", "°F", celsius_to_fahrenheit),
        '2': ("Enter Fahrenheit: ", "°F", "°C", fahrenheit_to_celsius),
        '3': ("Enter Celsius: ", "°C", "K", celsius_to_kelvin),
        '4': ("Enter Kelvin: ", "K", "°C", kelvin_to_celsius),
        '5': ("Enter Fahrenheit: ", "°F", "K", fahrenheit_to_kelvin),
        '6': ("Enter Kelvin: ", "K", "°F", kelvin_to_fahrenheit),
    }
    
    print("\n" + "="*45)
    print("   TEMPERATURE CONVERTER WITH KELVIN")
    print("   TEMPERATURE CONVERTER WITH KELVIN")
    print("="*45)
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")
    print("7. Exit")
    print("="*45)
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
        
        elif choice in conversions:
            try:
                prompt, in_unit, out_unit, func = conversions[choice]
                temp = float(input(prompt))
                result = func(temp)
                print(f"\n{temp}{in_unit} = {result:.2f}{out_unit}\n")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        else:
            print("Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()