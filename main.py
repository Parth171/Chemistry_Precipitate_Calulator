# main.py

"""
Title: Precipitate Calculator
Author: Parth Sakpal
date-created: 2022-10-20
"""


ELEMENT = "H"

ARRAY = [["H", 1.01, +1], ["He", 4.00, 0], ["Li", 6.94, +1], ["Be", 9.01, +2], []]

for i in range(len(ARRAY)):
    if ELEMENT == ARRAY[i][0]:
        print(f"{ARRAY[i][1]}, {ARRAY[i][2]}")
    else:
        pass
