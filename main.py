# main.py

"""
Title: Precipitate Calculator
Author: Parth Sakpal
date-created: 2022-10-20
"""

# --- VARIABLES --- #

# 2D array of the elements of the periodic table

ELEMENTS = (("H", 1.01, +1),
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
            ("Rb", 85.47, +1),
            ("Cs", 132.91, +1),
            ("Na", 22.99, +1),
            ("K", 39.10, +1),
            ("Fr", 223, +1),
            ("Sc", 44.96, +3),
            ("Y", 88.91, +3),
            ("La", 138.91, +3),
            ("Ac", 277, +3),
            ("Ti", 47.87, +4),
            ("Zr", 91.22, +4),
            ("Hf", 178.49, +4),
            ("V", 50.94, +5),
            ("Nb", 92.91, +5),
            ("Ta", 180.95, +5),
            ("Cr", 52.00, +3),
            ("Mo", 95.94, +6),
            ("W", 183.84, +6),
            ("Mn", 54.94, +2),
            ("Tc", 98, +7),
            ("Re", 186.21, +7),
            ("Ru", 101.07, +3),
            ("Os", 190.23, +4),
            ("Co", 58.93, +2),
            ("Rh", 102.91, +3),
            ("Ir", 192.22, +4),
            ("Ni", 58.69, +2),
            ("Pd", 106.42, +2),
            ("Pt", 195.08, +4),
            ("Au", 196.97, +3),
            ("Al", 26.98, +3),
            ("Ga", 69.72, +3),
            ("In", 114.82, +3),
            ("Ge", 72.64, +4),
            ("Sn", 118.71, +4),
            ("Sb", 121.76, +3),
            ("Bi", 208.98, +3),
            ("N", 14.01, -3),
            ("P", 30.97, -3),
            ("As", 74.92, -3),
            ("O", 16.00, -2),
            ("S", 32.07, -2),
            ("Se", 78.96, -2),
            ("Te", 127.6, -2),
            ("ClO4", 99.45, -1),
            ("CH3COO", 60.05, -1),
            ("SO4", 96.06, -2),
            ("OH", 17.008, -1),
            ("NH4", 18.04, +1),
            ("CO3", 100.0869, -2),
            ("PO4", 94.9714, -3),
            ("SO3", 80.06, -2),
            ("IO3", 174.903, -1),
            ("OOCCOO", 88.019, -2))

ELEMENT_1_LIST = []  # empty list to fill in information of positive reacting ion

ELEMENT_2_LIST = []  # empty list to fill in information of negative reacting ion

RUN = 0  # Variable to check if the code should run


### INPUTS

def Starting_Text():
    """
    Print out the starting text.
    :return: none
    """

    print("""

WELCOME TO PRECIPITATE CALCULATOR!

This program requires you to input two elements, and the volume and concentration of each element to determine the mass of their compound!


    """)


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

    for i in range(len(ELEMENTS)):
        if ELEMENT == ELEMENTS[i][0]:
            CHARGE = ELEMENTS[i][2]
            return int(CHARGE)


def Element_Molar_Mass(ELEMENT):
    """
    Determine the molar mass of the element
    :param ELEMENT: str
    :return: float
    """

    for i in range(len(ELEMENTS)):
        if ELEMENT == ELEMENTS[i][0]:
            MOLAR_MASS = ELEMENTS[i][1]
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
    Adds the components of the element to a list
    :param LIST: list
    :param ELEMENT: str
    :param COEFFICIENT: int
    :param MOL: float
    :param MASS: float
    :return: none
    """

    COEFFICIENT = abs(COEFFICIENT)

    LIST.append(COEFFICIENT)
    LIST.append(MOL)
    LIST.append(ELEMENT)
    LIST.append(MASS)


def Modify_List(LIST):
    """
    Changes the molar mass according to the coefficient of the element.
    :param LIST:
    :return:
    """

    MOLAR_MASS = LIST[0] * LIST[3]

    LIST[3] = MOLAR_MASS


def Compound_Mol(LIMITING_REAGENT_MOL, LIMITING_REAGENT_COEFFICIENT):
    """
    Determines the amount of mols of the compound
    :param LIMITING_REAGENT_MOL: float
    :param LIMITING_REAGENT_COEFFICIENT: int
    :return: float
    """

    MOL = (LIMITING_REAGENT_MOL) * (1 / LIMITING_REAGENT_COEFFICIENT)

    return MOL


def Precipitate_Mass(MOL, MOLAR_MASS):
    """
    Finds the mass of the precipitate
    :param MOL: float
    :param MOLAR_MASS: float
    :return: float
    """

    MASS = MOL * MOLAR_MASS

    MASS = round(MASS, 2)

    return MASS


if __name__ == "__main__":

    ### INPUTS

    ELEMENT_1 = Element_1()
    ELEMENT_1_VOLUME = Element_1_Volume()
    ELEMENT_1_CONCENTRATION = Element_1_Concentration()
    ELEMENT_1_MOL = Mol(ELEMENT_1_VOLUME, ELEMENT_1_CONCENTRATION)
    ELEMENT_1_CHARGE = Element_Charge(ELEMENT_1)
    ELEMENT_1_MASS = Element_Molar_Mass(ELEMENT_1)

    ELEMENT_2 = Element_2()
    ELEMENT_2_VOLUME = Element_2_Volume()
    ELEMENT_2_CONCENTRATION = Element_2_Concentration()
    ELEMENT_2_MOL = Mol(ELEMENT_2_VOLUME, ELEMENT_2_CONCENTRATION)
    ELEMENT_2_CHARGE = Element_Charge(ELEMENT_2)
    ELEMENT_2_MASS = Element_Molar_Mass(ELEMENT_2)

    ### PROCESSING

    # Checks table one of the solubility chart

    if ELEMENT_2 == "ClO4" and ELEMENT_1 == "Rb" or ELEMENT_1 == "Cs":
        RUN = 1

    if ELEMENT_2 == "NO3" or ELEMENT_2 == "ClO3" or ELEMENT_2 == "NH4" or ELEMENT_2 == "H" or ELEMENT_2 == "Li" or ELEMENT_2 == "Na" or ELEMENT_2 == "K" or ELEMENT_2 == "Rb" or ELEMENT_2 == "Cs" or ELEMENT_2 == "Fr":
        RUN = 0

    if ELEMENT_2 == "CH3COO" and ELEMENT_1 == "Ag":
        RUN = 1

    # Checks table two of the solubility chart

    if ELEMENT_2 == "F":
        if ELEMENT_1 == "Li" or ELEMENT_1 == "Mg" or ELEMENT_1 == "Ca" or ELEMENT_1 == "Sr" or ELEMENT_1 == "Ba" or ELEMENT_1 == "Fe" or ELEMENT_1 == "Pb":
            RUN = 1
        else:
            RUN = 0

    # Checks table three of the solubility chart

    if ELEMENT_2 == "Cl" or ELEMENT_2 == "Br" or ELEMENT_2 == "I":
        if ELEMENT_1 == "Cu" or ELEMENT_1 == "Ag" or ELEMENT_1 == "Pb" or ELEMENT_1 == "Tl":
            RUN = 1
        else:
            RUN = 0

    # Checks table four of the solubility chart

    if ELEMENT_2 == "SO4":
        if ELEMENT_1 == "Ca" or ELEMENT_1 == "Ag" or ELEMENT_1 == "Pb" or ELEMENT_1 == "Pb" or ELEMENT_1 == "Sr" or ELEMENT_1 == "Ba" or ELEMENT_1 == "Ra":
            RUN = 1
        else:
            RUN = 0

    # Checks table five of the solubility chart

    if ELEMENT_2 == "CO3" or ELEMENT_2 == "PO4" or ELEMENT_2 == "SO3":
        if ELEMENT_1 == "H" or ELEMENT_1 == "Li" or ELEMENT_1 == "Na" or ELEMENT_1 == "K" or ELEMENT_1 == "Rb" or ELEMENT_1 == "Cs" or ELEMENT_1 == "Fr" or ELEMENT_1 == "NH4":
            RUN = 0
        else:
            RUN = 1

    # Checks table six of the solubility chart

    if ELEMENT_2 == "IO3" or ELEMENT_2 == "OOCCOO":
        if ELEMENT_1 == "H" or ELEMENT_1 == "Li" or ELEMENT_1 == "Na" or ELEMENT_1 == "K" or ELEMENT_1 == "Rb" or ELEMENT_1 == "Cs" or ELEMENT_1 == "Fr" or ELEMENT_1 == "NH4":
            RUN = 0

    if ELEMENT_2 == "IO3" and ELEMENT_1 == "Co":
        RUN = 0

    if ELEMENT_2 == "OOCCOO" and ELEMENT_1 == "Fe":
        RUN = 0

    # Checks table seven of the solubility chart

    if ELEMENT_2 == "OH":
        if ELEMENT_1 == "H" or ELEMENT_1 == "Li" or ELEMENT_1 == "Na" or ELEMENT_1 == "K" or ELEMENT_1 == "Rb" or ELEMENT_1 == "Cs" or ELEMENT_1 == "Fr" or ELEMENT_1 == "NH4":
            RUN = 0
        else:
            RUN = 1

    if RUN == 1:  # if the reaction forms a precipitate

        Add_to_List(ELEMENT_1_LIST, ELEMENT_1, ELEMENT_2_CHARGE, ELEMENT_1_MOL, ELEMENT_1_MASS)

        Modify_List(ELEMENT_1_LIST)

        Add_to_List(ELEMENT_2_LIST, ELEMENT_2, ELEMENT_1_CHARGE, ELEMENT_2_MOL, ELEMENT_2_MASS)

        Modify_List(ELEMENT_2_LIST)

        LIMITING_REAGENT = Limiting_Reagent(ELEMENT_1_LIST, ELEMENT_2_LIST)

        # Determines which element is the limiting reagent
        if LIMITING_REAGENT == ELEMENT_1:
            LIMITING_REAGENT_MOL = ELEMENT_1_LIST[1]
            LIMITING_REAGENT_COEFFICIENT = ELEMENT_1_LIST[0]
        else:
            LIMITING_REAGENT_MOL = ELEMENT_2_LIST[1]
            LIMITING_REAGENT_COEFFICIENT = ELEMENT_2_LIST[0]

        # OUTPUTS

        print(f"The limiting reagent is {LIMITING_REAGENT}.")

        # Determines Compound Mol
        COMPOUND_MOL = Compound_Mol(LIMITING_REAGENT_MOL, LIMITING_REAGENT_COEFFICIENT)

        TOTAL_MOLAR_MASS = ELEMENT_1_LIST[3] + ELEMENT_2_LIST[3]

        MASS = Precipitate_Mass(COMPOUND_MOL, TOTAL_MOLAR_MASS)

        print(f"The mass of the precipitate is {MASS} g.")

    # If reaction does not form a precipitate

    elif RUN == 0:
        print("The two ions will not create a precipitate.")
