"""
CP1404 Practical
store users guitar input and print
"""

from guitar import Guitar


def main():
    """
    get information of guitars and print them
    """
    guitars = []  # create the list to store  guitar information
    # get_guitars(guitars)  # get user input of guitar information
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))    # for testing
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))   # for testing
    print_guitars(guitars)  # print guitar information


def print_guitars(guitars):
    """
    print guitar information stored in the guitars list
    """
    for i, guitar in enumerate(guitars):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


def get_guitars(guitars):
    """
    get guitar information including name, year and cost from user input
    """
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print("---------------------------------")
        name = input("Name: ")


main()
