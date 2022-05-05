#!/usr/bin/python3

# Author: Ethan Boswell
# Functions to convert functions to MBTI types and vice versa

# Judging functions:
# Te (extroverted thinking); Ti (introverted thinking)
# Fe (extroverted feeling); Fi (introverted feeling)

# Perceiving functions:
# Se (extroverted sensing); Si (introverted sensing)
# Ne (extroverted intuition); Ni (introverted intuition)

cognitive_functions = ["Te", "Fe", "Se", "Ne", "Ti", "Fi", "Si", "Ni"]

# Returns primary and secondary cognitive function in order based on
# MBTI type.
# Ex. INTJ returns (Ni, Te); ESTP returns (Se, Ti)
def get_cognitive_functions(type):
    type_1 = ""
    type_2 = ""

    # Perceiving function
    if type[1] == 'N':
        if type[3] == 'J':
            type_1 = "Ni"
        elif type[3] == 'P':
            type_1 = "Ne"
    elif type[1] == 'S':
        if type[3] == 'J':
            type_1 = "Si"
        elif type[3] == 'P':
            type_1 = "Se"

    # Judging function
    if type[2] == 'T':
        if type_1 == "Ni" or type_1 == "Si":
            type_2 = "Te"
        else:
            type_2 = "Ti"
    elif type[2] == 'F':
        if type_1 == "Ni" or type_1 == "Si":
            type_2 = "Fe"
        else:
            type_2 = "Fi"

    # ExxJ and IxxP types dominate with a judging function
    # IxxJ and ExxP types dominate with a perceiving function
    if (type[0] == 'E' and type[3] == 'J') or (type[0] == 'I' and type[3] == 'P'):
        return type_2, type_1
    else:
        return type_1, type_2

def get_mbti_type(primary, secondary):
    mbti_type = ""

    if primary[1] == 'e':
        mbti_type += 'E'
    else:
        mbti_type += 'I'

    if primary[0] == 'N' or primary[0] == 'S':
        mbti_type += primary[0]
        mbti_type += secondary[0]

    if secondary[0] == 'N' or primary[0] == 'S':
        mbti_type += secondary[0]
        mbti_type += primary[0]

    if mbti_type[0] == 'E' and (primary[0] == 'N' or primary[0] == 'S'):
        mbti_type += "P"
    if mbti_type[0] == 'I' and (primary[0] == 'T' or primary[0] == 'F'):
        mbti_type += "P"

    if len(mbti_type) == 3:
        mbti_type += "J"

    return mbti_type

# Convert a four-letter MBTI type to its primary and secondary cognitive function pair
def convert_to_cognitive_pair(type):
    functions = get_cognitive_functions(type)

    string = ""
    string += functions[0]
    string += functions[1]

    return string
