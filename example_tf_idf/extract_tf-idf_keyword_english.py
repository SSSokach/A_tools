from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import json
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


dataset=load_json('./train.json')
dataset=[one['dialog'] for one in dataset]
Q_corpus=[u for dialog in dataset for u in dialog]
print(Q_corpus[:20])
Q_vectorizer = TfidfVectorizer()  # 实例化
Q_vectorizer.fit(Q_corpus)  # 1.学习
Q_feature_words = Q_vectorizer.get_feature_names_out()
# print(Q_feature_words)
# print(len(Q_feature_words))
# exit()
for top_k in [2,3,4]:
    # top_k=1
    for name in ['dev','train','test']:
        dataset=load_json(f'{name}.json')
        for dialog in tqdm(dataset):
            key_words=[]
            for text in dialog['dialog']:
                x=Q_vectorizer.transform([text]).todense()  # 2.得到每一个text的tf-idf表示，用稀疏矩阵表示的
                x=[x[0,i] for i in range(x.shape[-1])]
                top_k_index=sorted(range(len(x)), key=x.__getitem__, reverse=True)[:top_k]
                if 0 in top_k_index:
                    top_k_index=top_k_index[:top_k_index.index(0)]
                # top_k_index=heapq.nlargest(top_k,range(len(x)),x.__getitem__)
                key_words.append([Q_feature_words[i] for i in top_k_index])  # 3.得到每个text tf-idf前五的词
            dialog['keywords']=key_words
        write_json(f'{top_k}_keywords/{name}_keywords.json',dataset)

