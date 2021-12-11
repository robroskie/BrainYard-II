

#https://goodboychan.github.io/python/datacamp/natural_language_processing/2020/07/17/04-TF-IDF-and-similarity-scores.html

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def removeFirstLastThree(text):
    text = text[3:]
    text = text[:len(text)-3]
    return text


def applyPStemmer_df(text):

    ps = PorterStemmer()

    stemmed_words=[]

    for w in text:
        stemmed_words.append(ps.stem(w))

    return stemmed_words


def prepare_LDA_df(text):

    return word_tokenize(text)

def getCSim(text):

    text_file = 'Data\dfPostsRandomQuestionsDec9.csv'





    df = pd.read_csv(text_file, encoding='utf-8', low_memory=False)
    df = df.head(5000)

    df = df[['Id', 'Body']]
    df = df[df['Body'].notna()]

    # df['Body'] = df['Body'].astype(str)
    df['Body'] = df.apply(lambda x: removeFirstLastThree(x['Body']), axis=1)

    # df['Body'] = df.apply(lambda x: prepare_LDA_df(x['Body']), axis=1)

    # df.reset_index(drop=True, inplace=True)



    toAdd = {'Body_q' : text}

    df_input = pd.DataFrame()


    for z in range(0,len(df.index)):
        df_input = df_input.append(toAdd, ignore_index=True)


    # print(df.head())




    


    df.loc[-1] = [-1, text]  # adding a row
    df.index = df.index + 1  # shifting index
    df.sort_index(inplace=True) 

    
    # print(df.head())


    # This list was adapted from:
    # https://reversedictionary.org/wordsfor/(computer%20science)%20a%20list%20of%20options%20available%20to%20a%20computer%20user
    features = []

    # # # VVVVVVVVVVVVVVVVVVVVVVVV
    # cssim = cosine_similarity(dfcs, dfcs)

    # with open("Data/keywords.txt", "r") as wordList:
    #     lines = wordList.readlines()
    #     for i in lines:
    #         to_list = i.split('\n')
    #         features.append(to_list[0])

    cv = CountVectorizer(stop_words = 'english', min_df=5, max_features=500)
    count_matrix = cv.fit_transform(df['Body'])
    # print(df['Body'].head())
    count_matrix

    counts = pd.DataFrame(count_matrix.toarray(), columns=cv.get_feature_names())
    # print(counts)

    # counts.to_csv('useless.csv', encoding = 'utf-8')

    cosine_sim = cosine_similarity(count_matrix)

    closest_Q = list(enumerate(cosine_sim[0]))
    
 
    # print(closest_Q)


    sorted_similar = sorted(closest_Q, key=lambda x:x[1], reverse=True)
    # print(sorted_similar)
    # (2, 5)
    sorted_similar = sorted_similar[1:6]
    # print(sorted_similar)

    to_return = []
    i = 0
    for q in sorted_similar:
        # print(df['Body'][q[0]])
        to_return.append("<strong>Question {}</strong><br>:  {}".format(i, str(df['Body'][q[0]])))
        i += 1
        

    # print(to_return)

    # print('to return costin .py')
    # print(to_return)
    return to_return
# getCSim('would like to know how i can initialize an array(or list), yet to be populated with values, to have a defined size')