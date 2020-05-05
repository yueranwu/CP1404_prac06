"""CP1404 Practical - client code to use the ProgrammingLanguage class"""

from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)
    print("---------------------------")

    dynamically_language(python, ruby, visual_basic)    # check if dynamical


def dynamically_language(python, ruby, visual_basic):
    """
    check and print the name of dynamical programming language
    """
    languages = [ruby, python, visual_basic]  # store programming languages into the list
    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
