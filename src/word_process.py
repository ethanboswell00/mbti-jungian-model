#!/usr/bin/python3

# Author: Ethan Boswell
# NLP implementation of MBTI personality predictions using dominant and auxiliary cognitive functions

# Judging functions:
# Te (extroverted thinking); Ti (introverted thinking)
# Fe (extroverted feeling); Fi (introverted feeling)

# Perceiving functions:
# Se (extroverted sensing); Si (introverted sensing)
# Ne (extroverted intuition); Ni (introverted intuition)

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import mbti

statement_list = []
full_types_list = []

# Load MBTI data from .csv file containing types and a list of their posts.
# Tokenizes posts, removes stop words, stems and tags words.
def process_data(filename):
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    with open(filename) as f:
        header = f.readline()
        types = []
        posts = []
        for line in f.readlines():
            # Split posts by ||| in data set
            data = line.split(',')
            temp_type = mbti.convert_to_cognitive_pair(data[0])
            types.append(temp_type)
            all_posts = data[1].split('|||')
            all_posts[0] = all_posts[0][2:]

            # Tokenize, remove stop words, lemmatize, and set all words to lowercase in posts
            for i in range(len(all_posts)):
                all_posts[i] = nltk.word_tokenize(all_posts[i])
                all_posts[i] = [word for word in all_posts[i] if word not in stop_words]
                all_posts[i] = [lemmatizer.lemmatize(word) for word in all_posts[i]]
                all_posts[i] = [word.lower() for word in all_posts[i]]
                all_posts[i] = ' '.join(all_posts[i])
                statement_list.append(all_posts[i])
                full_types_list.append(temp_type)
            posts.append(all_posts)
        return types, posts
