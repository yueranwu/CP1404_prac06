"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print("---------------------------------------------------------------------------")

    limo = Car("Limo", 100)     # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo.add_fuel(20)   # Add 20 more units of fuel to this new car object using the add method.
    print("Limo's fuel = ", limo.fuel)  # Print the amount of fuel in the car.
    limo.drive(115)     # Attempt to drive the car 115km using the drive method.
    print("Limo's odometer: ", limo.odometer)   # Print the car's odometer reading.
    print(limo)


main()