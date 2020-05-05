"""CP1404 testing Guitar class"""

from guitar import Guitar


def main():
    """

    check if get_age() and is_vintage function work properly in Guitar class
    """
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 1000.55)

    print("{} get_age() - Expected 98. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another.name, another.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another.name, another.is_vintage()))


main()
