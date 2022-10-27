# main.py

"""
Title: Precipitate Calculator
Author: Parth Sakpal
date-created: 2022-10-20
"""


ARRAY = [["H", 1.01, +1],
         ["He", 4.00, 0],
         ["Li", 6.94, +1],
         ["Be", 9.01, +2],
         ["F", 19.0, -1],
         ["Cl", 35.45, -1]]

ELEMENT_1 = []

ELEMENT_2 = []

def Element_Charge(ELEMENT):

    """
    Find the elements charge
    :param ELEMENT: String
    :return: int
    """

    for i in range(len(ARRAY)):
        if ELEMENT == ARRAY[i][0]:
            CHARGE = ARRAY[i][2]
        else:
            pass

    return CHARGE


def Element_Molar_Mass(ELEMENT):

    """
    Checks to figure out the elements molar mass
    :param ELEMENT: String
    :return: float
    """

    for i in range(len(ARRAY)):
        if ELEMENT == ARRAY[i][0]:
            MOLAR_MASS = ARRAY[i][1]
        else:
            pass

    return MOLAR_MASS

if __name__ == "__main__":

    USER_INPUT_1 = input("Enter your first element: ")

    ELEMENT_1.append(USER_INPUT_1)

    ELEMENT1_MOLAR_MASS = Element_Molar_Mass(USER_INPUT_1)

    ELEMENT_1.append(ELEMENT1_MOLAR_MASS)

    ELEMENT1_CHARGE = Element_Charge(USER_INPUT_1)

    ELEMENT_1.append(ELEMENT1_CHARGE)

    print(ELEMENT_1)



    print(f"The molar mass of {USER_INPUT_1} is {ELEMENT1_MOLAR_MASS} and the charge is {ELEMENT1_CHARGE}")


    USER_INPUT_2 = input("Enter you second element: ")

    ELEMENT_2.append(USER_INPUT_2)

    ELEMENT2_MOLAR_MASS = Element_Molar_Mass(USER_INPUT_2)

    ELEMENT_2.append(ELEMENT1_MOLAR_MASS)

    ELEMENT2_CHARGE = Element_Charge(USER_INPUT_2)

    ELEMENT_2.append(ELEMENT2_CHARGE)

    print(ELEMENT_2)

    print(f"The molar mass of {USER_INPUT_2} is {ELEMENT2_MOLAR_MASS} and the charge is {ELEMENT2_CHARGE}")






