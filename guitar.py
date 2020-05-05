"""CP1404 Practical define Guitar class"""


class Guitar:

    def __init__(self, name, year, cost):
        """
        Initiate a guitar instance

        name: string, name of the guitar
        year: int, the year when the guitar is produced
        cost: int, money needed for buying the guitar
        """
        self.name = name
        self.year = year
        self. cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        """
        returns how old the guitar is in years
        """
        age = 2020 - self.year
        return age

    def is_vintage(self):
        """
         returns True if the guitar is 50 or more years old, False otherwise
        """
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False

