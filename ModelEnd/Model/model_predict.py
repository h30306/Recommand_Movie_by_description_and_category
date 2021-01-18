import pickle
import os
import numpy as np
import pandas as pd
from bert_serving.client import BertClient


def selsect_movie(vector, pretrained_vector):
    corr_matrix = np.corrcoef(vector, pretrained_vector)[0][:-1]
    top_movie_id = sorted(range(len(corr_matrix)), key=lambda i: corr_matrix[i])[-10:]
    top_movie_id.reverse()
    return top_movie_id

def predict_vector(sentence, dont_like_movie):
    df = pd.read_csv('./Model/data/IMDB_movie_V1_clear.csv')
    dict_ = {}
    try:
        bc = BertClient()
        print('BERT ok')
        if os.path.exists('./Model/data/BERT.npy'):
            bert_embedding = np.load(open('./Model/data/BERT.npy', 'rb'))
            sentence_embedding = bc.encode([sentence])
            print('Encode done')
            for i,v in enumerate(selsect_movie(sentence_embedding, bert_embedding)):
                dict_[v] = i
        else:
            print('No Pretrained Movie Embedding')
    except:
        print('BERT Client server not start')

    if os.path.exists('./Model/data/vectorizer.pickle') & os.path.exists('./Model/data/TFIDF.npy'):
        vectorizer = pickle.load(open('./Model/data/vectorizer.pickle', "rb"))
        tfidf_vector = np.load(open('./Model/data/TFIDF.npy', "rb"))
        sentence_vector = vectorizer.transform([sentence]).toarray()
        for i,v in enumerate(selsect_movie(sentence_vector, tfidf_vector)):
            if v in dict_:
                dict_[v] = (dict_[v]+i)/2
            else:
                dict_[v] = i
    else:
        print('No Pretrained Movie Vector')

    dlist = list(dict_.keys())
    for movie_id in dlist:
        if df.loc[movie_id]['category'] in set(dont_like_movie):
            del dict_[movie_id]
    sort = {k: v for k, v in sorted(dict_.items(), key=lambda item: item[1])}.keys()
    recommend = df.ix[sort]
    return recommend.to_dict('list')
    