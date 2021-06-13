from calculator import Calculator

def main():

    print(
        """
        This application demonstrates how much that will be spent during a trip, using as 
        a base the consumption of your vehicle and the chosen distance!
        """
        )

    print("The available fuels to this calculation are: ")
    print("     ° Alcohol")
    print("     ° Gasoline")
    print("     ° Diesel")

    print(" ")

    try:
        distance = float(input("Distance to be traveled in kilometres\n"))
        consumption = float(input("Fuel consumption of the veihcle(Km/l)\n"))
        calculator = Calculator()
        print(
            calculator.spent_calculate(distance, consumption)
        )
    except ValueError as erro:
        print("The value received is not valid")
    
if __name__ == "__main__":
    main()