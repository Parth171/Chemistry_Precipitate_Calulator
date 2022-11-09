# main.py

"""
Title: Precipitate Calculator
Author: Parth Sakpal
date-created: 2022-10-20
"""

# --- VARIABLES --- #

RUN = 0

ARRAY = (("H", 1.01, +1),
         ("He", 4.00, 0),
         ("Li", 6.94, +1),
         ("Be", 9.01, +2),
         ("F", 19.0, -1),
         ("Cl", 35.45, -1),
         ("Pb", 207.20, +2),
         ("Cu", 63.55, +1),
         ("Br", 79.90, -1),
         ("Mg", 24.31, +2),
         ("Ca", 40.08, +2),
         ("Sr", 87.62, +2),
         ("Ba", 137.33, +2),
         ("Fe", 55.85, +2),
         ("I", 126.90, -1),
         ("Ag", 107.87, +1),
         ("Tl", 204.38, +1),
         ("Ra", 226, +2),
         ("SO4", 96.06, -2),
         ("Rb", 85.47, +1),
         ("Cs", 132.91, +1),
         ("ClO4", 99.45, -1),
         ("CH3COO", 60.05, -1))

ELEMENT_1_LIST = []

ELEMENT_2_LIST = []


### INPUTS

def Element_1():

    """
    Asks user for positive reacting ion
    :return: str
    """



    ELEMENT_1 = input("Please enter the positive reacting ion. (no charges) ")

    return ELEMENT_1


def Element_2():

    """
    Asks user for negative reacting ion
    :return: str
    """



    ELEMENT_2 = input("Please enter the negative reacting ion. (no charges) ")

    return ELEMENT_2


def Element_1_Volume():

    """
    Asks user for the volume of the positive reacting ion
    :return: float
    """

    VOLUME = input("What is the volume of the positive solution? (L) ")

    return float(VOLUME)


def Element_2_Volume():

    """
    Asks user for the volume of the negative reacting ion
    :return: float
    """

    VOLUME = input("What is the volume of the negative solution? (L) ")

    return float(VOLUME)


def Element_1_Concentration():

    """
    Asks user for the concentration of the positive reacting ion
    :return: float
    """

    CONCENTRATION = input("What is the volume of the positive solution? (mol/L) ")

    return float(CONCENTRATION)


def Element_2_Concentration():

    """
    Asks user for the concentration of the negative reacting ion
    :return: float
    """
    CONCENTRATION = input("What is the volume of the negative solution? (mol/L) ")

    return float(CONCENTRATION)


### PROCESSING

def Element_Charge(ELEMENT):

    """
    Determines the charge of the element
    :param ELEMENT: str
    :return: int
    """



    for i in range(len(ARRAY)):
        if ELEMENT == ARRAY[i][0]:
            CHARGE = ARRAY[i][2]
            return int(CHARGE)


def Element_Molar_Mass(ELEMENT):

    """
    Determine the molar mass of the element
    :param ELEMENT: str
    :return: float
    """

    for i in range(len(ARRAY)):
        if ELEMENT == ARRAY[i][0]:
            MOLAR_MASS = ARRAY[i][1]
            return float(MOLAR_MASS)


def Mol(VOLUME, CONCENTRATION):

    """
    Determine the amount of mols, using the volume and concentration
    :param VOLUME: float
    :param CONCENTRATION: float
    :return: float
    """
    MOL = VOLUME * CONCENTRATION

    return MOL


def Limiting_Reagent(LIST_1, LIST_2):

    """
    Determine the limiting reagent of the reaction
    :param LIST_1: list
    :param LIST_2: list
    :return:
    """

    ELEMENT_1 = LIST_1[1] / LIST_1[0]

    ELEMENT_2 = LIST_2[1] / LIST_2[0]

    if ELEMENT_1 < ELEMENT_2:
        Limiting_Reagent = LIST_1[2]
    else:
        Limiting_Reagent = LIST_2[2]
    return Limiting_Reagent


def Add_to_List(LIST, ELEMENT, COEFFICIENT, MOL, MASS):
    """
    Adds the components of the element to the list
    """

    COEFFICIENT = abs(COEFFICIENT)

    LIST.append(COEFFICIENT)
    LIST.append(MOL)
    LIST.append(ELEMENT)
    LIST.append(MASS)

def Modify_List(LIST):

    """

    :param LIST: list
    :return: none
    """


    MOLAR_MASS = LIST[0] * LIST[3]

    LIST[3] = MOLAR_MASS


def Compound_Mol(LIMITING_REAGENT_MOL, LIMITING_REAGENT_COEFFICIENT):
    """
    Calculates the mol of the entire compound
    """

    MOL = (LIMITING_REAGENT_MOL) * (1 / LIMITING_REAGENT_COEFFICIENT)

    return MOL


def Precipitate_Mass(MOL, MOLAR_MASS):
    """
    finds mass of precipitate
    """

    MASS = MOL * MOLAR_MASS

    MASS = round(MASS, 2)

    return MASS


if __name__ == "__main__":

    ELEMENT_1 = Element_1()
    ELEMENT_1_VOLUME = Element_1_Volume()
    ELEMENT_1_CONCENTRATION = Element_1_Concentration()
    ELEMENT_1_MOL = Mol(ELEMENT_1_VOLUME, ELEMENT_1_CONCENTRATION)
    ELEMENT_1_CHARGE = Element_Charge(ELEMENT_1)
    ELEMENT_1_MASS = Element_Molar_Mass(ELEMENT_1)
    # print(ELEMENT_1_CHARGE)

    ELEMENT_2 = Element_2()
    ELEMENT_2_VOLUME = Element_2_Volume()
    ELEMENT_2_CONCENTRATION = Element_2_Concentration()
    ELEMENT_2_MOL = Mol(ELEMENT_2_VOLUME, ELEMENT_2_CONCENTRATION)
    ELEMENT_2_CHARGE = Element_Charge(ELEMENT_2)
    ELEMENT_2_MASS = Element_Molar_Mass(ELEMENT_2)
    # print(ELEMENT_2_CHARGE)

    if ELEMENT_2 == "F":
        if ELEMENT_1 == "Li" or ELEMENT_1 == "Mg" or ELEMENT_1 == "Ca" or ELEMENT_1 == "Sr" or ELEMENT_1 == "Ba" or ELEMENT_1 == "Fe" or ELEMENT_1 == "Pb":
            RUN = 1
        else:
            RUN = 0

    if ELEMENT_2 == "Cl" or ELEMENT_2 == "Br" or ELEMENT_2 == "I":
        if ELEMENT_1 == "Cu" or ELEMENT_1 == "Ag" or ELEMENT_1 == "Pb" or ELEMENT_1 == "Tl":
            RUN = 1
        else:
            RUN = 0

    if ELEMENT_2 == "SO4":
        if ELEMENT_1 == "Ca" or ELEMENT_1 == "Ag" or ELEMENT_1 == "Pb" or ELEMENT_1 == "Pb" or ELEMENT_1 == "Sr" or ELEMENT_1 == "Ba" or ELEMENT_1 == "Ra":
            RUN = 1
        else:
            RUN = 0

    if ELEMENT_2 == "ClO4" and ELEMENT_1 == "Rb" or ELEMENT_1 == "Cs":
        RUN = 1

    if ELEMENT_2 == "CH3COO" and ELEMENT_1 == "Ag":
        RUN = 1

    if ELEMENT_2 == "NO3" or ELEMENT_2 == "ClO3" or ELEMENT_2 == "NH4" or ELEMENT_2 == "H" or ELEMENT_2 == "Li" or ELEMENT_2 == "Na" or ELEMENT_2 == "K" or ELEMENT_2 == "Rb" or ELEMENT_2 == "Cs" or ELEMENT_2 == "Fr":
        RUN = 0

    if RUN == 1:

        Add_to_List(ELEMENT_1_LIST, ELEMENT_1, ELEMENT_2_CHARGE, ELEMENT_1_MOL, ELEMENT_1_MASS)

        Modify_List(ELEMENT_1_LIST)

        print(ELEMENT_1_LIST)

        Add_to_List(ELEMENT_2_LIST, ELEMENT_2, ELEMENT_1_CHARGE, ELEMENT_2_MOL, ELEMENT_2_MASS)

        Modify_List(ELEMENT_2_LIST)

        print(ELEMENT_2_LIST)

        LIMITING_REAGENT = Limiting_Reagent(ELEMENT_1_LIST, ELEMENT_2_LIST)

        if LIMITING_REAGENT == ELEMENT_1:
            LIMITING_REAGENT_MOL = ELEMENT_1_LIST[1]
            LIMITING_REAGENT_COEFFICIENT = ELEMENT_1_LIST[0]
        else:
            LIMITING_REAGENT_MOL = ELEMENT_2_LIST[1]
            LIMITING_REAGENT_COEFFICIENT = ELEMENT_2_LIST[0]

        print(f"{LIMITING_REAGENT} is the LIMITING_REAGENT")

        COMPOUND_MOL = Compound_Mol(LIMITING_REAGENT_MOL, LIMITING_REAGENT_COEFFICIENT)

        TOTAL_MOLAR_MASS = ELEMENT_1_LIST[3] + ELEMENT_2_LIST[3]
        print(f"{TOTAL_MOLAR_MASS} - total mass")
        print(COMPOUND_MOL)

        MASS = Precipitate_Mass(COMPOUND_MOL, TOTAL_MOLAR_MASS)
        print(MASS)

    elif RUN == 0:
        print("No precipitate")






