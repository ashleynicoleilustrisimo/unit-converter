def perform_conversion(value, from_unit, to_unit):
    # Conversion factors dictionary
    conversions = {
        'length': {
            'meters': 1.0,
            'feet': 3.28084,
            'inches': 39.3701
        },
        'weight': {
            'kilograms': 1.0,
            'pounds': 2.20462,
            'ounces': 35.274
        },
        'temperature': {
            'celsius': 'C',
            'fahrenheit': 'F'
        }
    }
    
    # Special case for temperature
    if 'temperature' in [from_unit[0], to_unit[0]]:
        if from_unit[1] == 'celsius' and to_unit[1] == 'fahrenheit':
            return (value * 9/5) + 32
        elif from_unit[1] == 'fahrenheit' and to_unit[1] == 'celsius':
            return (value - 32) * 5/9
        else:
            return value
    
    # Regular conversion for length and weight
    category = from_unit[0]
    if category == to_unit[0]:
        factor_from = conversions[category][from_unit[1]]
        factor_to = conversions[category][to_unit[1]]
        return value * (factor_to / factor_from)
    else:
        return None

def main():
    print("Welcome to Unit Converter!")
    
    # Available conversion types
    categories = {
        1: ('length', ['meters', 'feet', 'inches']),
        2: ('weight', ['kilograms', 'pounds', 'ounces']),
        3: ('temperature', ['celsius', 'fahrenheit'])
    }
    
    while True:
        # Step 1: Input value
        try:
            value = float(input("Enter the value to convert: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Step 2: Select units
        print("\nAvailable categories:")
        for num, (category, units) in categories.items():
            print(f"{num}. {category.capitalize()}")
        
        try:
            category_choice = int(input("Choose category (1-3): "))
            if category_choice not in categories:
                raise ValueError
        except ValueError:
            print("Please enter a valid category number.")
            continue
        
        category, units = categories[category_choice]
        
        print(f"\nAvailable units for {category}:")
        for i, unit in enumerate(units, 1):
            print(f"{i}. {unit.capitalize()}")
        
        try:
            from_unit = int(input(f"Convert from (1-{len(units)}): "))
            to_unit = int(input(f"Convert to (1-{len(units)}): "))
            if from_unit < 1 or from_unit > len(units) or to_unit < 1 or to_unit > len(units):
                raise ValueError
        except ValueError:
            print("Please enter valid unit numbers.")
            continue
        
        # Step 3: Perform calculation
        result = perform_conversion(
            value, 
            (category, units[from_unit-1]), 
            (category, units[to_unit-1])
        )
        
        # Step 4: Output result
        if result is not None:
            print(f"\n{value} {units[from_unit-1]} = {result:.4f} {units[to_unit-1]}")
        else:
            print("Invalid conversion.")
        
        # Ask if user wants to convert again
        if input("\nWould you like to convert another value? (yes/no): ").lower() != 'yes':
            break
    
    print("Thank you for using Unit Converter!")

if __name__ == "__main__":
    main()
