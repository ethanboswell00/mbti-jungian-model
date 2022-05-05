#!/usr/bin/python3

# Author: Ethan Boswell
# NLP implementation of MBTI personality predictions using dominant and auxiliary cognitive functions

# Judging functions:
# Te (extroverted thinking); Ti (introverted thinking)
# Fe (extroverted feeling); Fi (introverted feeling)

# Perceiving functions:
# Se (extroverted sensing); Si (introverted sensing)
# Ne (extroverted intuition); Ni (introverted intuition)

import word_process, train, predict, graph

def measure_accuracy(set, predictions):
    accuracy = 0.0
    total_correct = 0
    total_values = len(set)

    for i in range(len(set)):
        if set[i] == predictions[i]:
            total_correct += 1

    accuracy = (total_correct / total_values)

    return accuracy

def main():
    types, posts = word_process.process_data("../data/mbti_1.csv")
    vectorizer = train.vectorize_lists()
    tree_quantities = [5, 10, 50, 100, 200]
    standard_accuracies = []
    my_accuracies = []
    for i in range(5):
        classifier, test_list, actual_labels = train.train_sets(vectorizer, tree_quantities[i])
        standard_predictions, my_predictions = predict.predict_sets(classifier, test_list)

        std_acc = measure_accuracy(actual_labels, standard_predictions)
        my_acc = measure_accuracy(actual_labels, my_predictions)
        print(str(tree_quantities[i]) + "-tree accuracy with standard random forest classification:")
        print(std_acc)
        print(str(tree_quantities[i]) + "-tree accuracy with customized cognitive MBTI algorithm:")
        print(my_acc)

        standard_accuracies.append(std_acc)
        my_accuracies.append(my_acc)

    graph.plot_data(standard_accuracies, my_accuracies, tree_quantities)

if __name__ == '__main__':
    main()
