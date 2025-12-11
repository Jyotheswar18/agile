def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("\n" + "="*40)
    print("CELSIUS TO FAHRENHEIT CONVERTER")
    print("="*40)
    
    while True:
        try:
            celsius = float(input("\nEnter temperature in Celsius (or 'q' to quit): "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            user_input = input("\nEnter temperature in Celsius (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            else:
                print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()