from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import json
import jieba
import numpy as np
import heapq
from tqdm import tqdm
def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

dataset=load_json('./jddc_sessions.json')
Q_corpus=[u['sens'] for session in dataset for u in session if u['person']=='Q']
Q_corpus=[' '.join(list(jieba.cut(t, cut_all=True))) for t in Q_corpus]
Q_vectorizer = TfidfVectorizer()  # 实例化
Q_vectorizer.fit(Q_corpus)
Q_feature_words = Q_vectorizer.get_feature_names_out()

A_corpus=[u['sens'] for session in dataset for u in session if u['person']=='A']
A_corpus=[' '.join(list(jieba.cut(t, cut_all=True))) for t in A_corpus]
A_vectorizer = TfidfVectorizer()  # 实例化
A_vectorizer.fit(A_corpus)
A_feature_words = A_vectorizer.get_feature_names_out()


top_k=5
for session in tqdm(dataset):
    for utterance in session:
        text=utterance['sens']
        person=utterance['person']
        cut_list=[' '.join(list(jieba.cut(text, cut_all=True)))]
        if person=='Q':
            x=Q_vectorizer.transform(cut_list).todense()
            x=[x[0,i] for i in range(x.shape[-1])]
            top_k_index=sorted(range(len(x)), key=x.__getitem__, reverse=True)[:top_k]
            if 0 in top_k_index:
                top_k_index=top_k_index[:top_k_index.index(0)]
            # top_k_index=heapq.nlargest(top_k,range(len(x)),x.__getitem__)
            top_k_word=[Q_feature_words[i] for i in top_k_index]
        elif person=='A':
            x=A_vectorizer.transform(cut_list).todense()
            x=[x[0,i] for i in range(x.shape[-1])]
            top_k_index=sorted(range(len(x)), key=x.__getitem__, reverse=True)[:top_k]
            if 0 in top_k_index:
                top_k_index=top_k_index[:top_k_index.index(0)]
            # top_k_index=heapq.nlargest(top_k,range(len(x)),x.__getitem__)
            top_k_word=[A_feature_words[i] for i in top_k_index]
        else:
            print('error')
        utterance['keywords']='关键词：'+'，'.join(top_k_word)

write_json('./jddc_sessions_keyword.json',dataset)

