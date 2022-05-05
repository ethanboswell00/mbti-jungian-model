#!/usr/bin/python3

# Author: Ethan Boswell
# NLP implementation of MBTI personality predictions using dominant and auxiliary cognitive functions

# Judging functions:
# Te (extroverted thinking); Ti (introverted thinking)
# Fe (extroverted feeling); Fi (introverted feeling)

# Perceiving functions:
# Se (extroverted sensing); Si (introverted sensing)
# Ne (extroverted intuition); Ni (introverted intuition)

import matplotlib.pyplot as plt

def plot_data(standard_accuracies, my_accuracies, tree_quantities):
    plt.plot(standard_accuracies, label='Standard Prediction')
    plt.plot(my_accuracies, label='Cognitive Function Average')

    plt.title('Prediction accuracies on standard vs function algorithm')
    plt.ylabel('Prediction accuracy')
    plt.xlabel('# of Decision Trees')
    plt.show()
    plt.savefig('figure.png')
