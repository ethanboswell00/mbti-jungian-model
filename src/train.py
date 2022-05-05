#!/usr/bin/python3

# Author: Ethan Boswell
# NLP implementation of MBTI personality predictions using dominant and auxiliary cognitive functions

# Judging functions:
# Te (extroverted thinking); Ti (introverted thinking)
# Fe (extroverted feeling); Fi (introverted feeling)

# Perceiving functions:
# Se (extroverted sensing); Si (introverted sensing)
# Ne (extroverted intuition); Ni (introverted intuition)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from word_process import statement_list, full_types_list

def vectorize_lists():
    cv = CountVectorizer(max_features=5000)
    vectorizer = cv.fit_transform(statement_list).toarray()
    return vectorizer

def train_sets(vectorizer, num_trees):
    X_train, X_test, y_train, y_test = train_test_split(vectorizer, full_types_list, test_size=0.25, random_state=0)
    classifier = RandomForestClassifier(n_estimators=num_trees, criterion="entropy", random_state=0)
    classifier.fit(X_train, y_train)
    test_list = X_test
    return classifier, test_list, y_test
