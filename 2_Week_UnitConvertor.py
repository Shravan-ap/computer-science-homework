def alert(text):
    print("\n")
    print("-" * (len(text)))
    print(text.upper())
    print("-" * len(text))
    print("\n")


def main_menu():
    conversions = {

        "1": ("Kilometers to Miles", 0.621371, 0),

        "2": ("Miles to Kilometers", 1 / 0.621371, 0),

        "3": ("Celsius to Fahrenheit", 9 / 5, 32),

        "4": ("Fahrenheit to Celsius", 5 / 9, -32 * 5 / 9),

        "5": ("Meters to Yards", 1.0936133, 0),

        "6": ("Yards to Meters", 0.9144, 0)
    }
    for number, (name, _, _) in conversions.items():
        print(f"{number}. {name}")
    choice = input("\n Choose a conversion: ")
    if choice in conversions:
        try:
            value = float(input("\nEnter the value: "))
            name, factor, offset = conversions[choice]
            result = global_conversions(value, factor, offset)
            print(f"\n Result: {result}")
        except ValueError:
            print("\nPlease enter a number.")
    else:
        print("\n Invalid choice, Enter conversions\n")
        main_menu()


def global_conversions(value, factor, offset=0):
    return value * factor + offset


def try_unit_again():
    y_n = input("\nWould you like to try again? (y/n): \n").strip().lower()
    if y_n == 'y':
        main_menu()
    elif y_n == 'n':
        alert("Thanks for using the Convertor")
        exit()
    else:
        print("Invalid input")
        try_unit_again()


def main():
    alert("Welcome to the unit convertor")
    main_menu()
    try_unit_again()


main()
