"""CP1404/CP5632 Practical define ProgrammingLanguage class"""


class ProgrammingLanguage:
    """represent a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Initiate a programming language instance

            name: string, the name of programming language
            typing: string, the typing of programming language is dynamic or static
            reflection: string,
            year:
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {}, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """
        returns True/False if the programming language is dynamically typed or not
        """
        if self.typing == "Dynamic":
            return True
        else:
            return False
