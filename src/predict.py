#!/usr/bin/python3

# Author: Ethan Boswell
# NLP implementation of MBTI personality predictions using dominant and auxiliary cognitive functions

# Judging functions:
# Te (extroverted thinking); Ti (introverted thinking)
# Fe (extroverted feeling); Fi (introverted feeling)

# Perceiving functions:
# Se (extroverted sensing); Si (introverted sensing)
# Ne (extroverted intuition); Ni (introverted intuition)

alphabetical_list = ["FeNi", "FeSi", "FiNe", "FiSe", "NeFi", "NeTi", "NiFe", "NiTe", "SeFi", "SeTi", "SiFe", "SiTe", "TeNi", "TeSi", "TiNe", "TiSe"]

# Make MBTI predictions on a set of posts.
# Using the current random forest classifier to predict on a test list
# Since the classifier sorts the labels in alphabetical order, the predictions
# will occur in the following order via predict_proba:

# FeNi, FeSi, FiNe, FiSe,
# NeFi, NeTi, NiFe, NiTe,
# SeFi, SeTi, SiFe, SiTe,
# TeNi, TeSi, TiNe, TiSe
def predict_sets(classifier, test_list):
    standard_predictions = classifier.predict(test_list)
    my_predictions = classifier.predict_proba(test_list)
    my_labels = []

    # Based on the order described above, looks through the list of
    # predicted values and averages them. For the primary cognitive function,
    # the highest average value is determined to be the primary function.
    for pred in my_predictions:
        primary_index = primary(pred)
        secondary_index = secondary(pred, primary_index)

        my_pred = make_prediction(primary_index, secondary_index)
        my_labels.append(my_pred)

    return standard_predictions, my_labels

# Get the average of each primary cognitive function prediction value and
# return the highest value and its index
def primary(prediction):
    primary_pred_value = 0.0
    tmp_value = 0.0
    index_found = 0

    for i in range(len(prediction)):
        if i % 2 == 1:
            continue
        tmp_value = (prediction[i] + prediction[i + 1]) / 2

        if tmp_value > primary_pred_value:
            primary_pred_value = tmp_value
            index_found = i

    return index_found

def secondary(prediction, primary_index):
    secondary_pred_value = 0.0
    secondary_index = 0

    if primary_index < 8:
        if primary_index < 4:
            secondary_index = primary_index + 12
        else:
            secondary_index = primary_index + 4
    else:
        if primary_index < 12:
            secondary_index = primary_index - 4
        else:
            secondary_index = primary_index - 12

    if prediction[secondary_index] > prediction[secondary_index + 1]:
        secondary_index += 1
    secondary_pred_value = prediction[secondary_index]

    return secondary_index

def make_prediction(primary_index, secondary_index):
    if secondary_index % 2 == 1:
        if primary_index % 2 == 0:
            primary_index += 1
    else:
        if primary_index % 2 == 1:
            primary_index -= 1

    return alphabetical_list[primary_index]
