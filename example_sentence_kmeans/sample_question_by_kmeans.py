import os
import random
random.seed(1234)
from utils import *
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import json
import matplotlib.pyplot as plt
root_path='/home/shilongwang/workplace/A_tools/sentence_kmeans/sentences1'

num_clusters = 10
corpus = []
dataset=load_json(f'{root_path}/result.json')

mode='title'
corpus=[one['title'] for one in dataset]
# mode='abstract'
# corpus=[one['abstract'] for one in dataset]
# mode='all'
# corpus=[one['title']+'\n'+one['abstract'] for one in dataset]

if not os.path.exists(f'{root_path}/corpus_embeddings_{mode}.pkl'):
    from sentence_transformers import SentenceTransformer
    encoder = SentenceTransformer('/home/shilongwang/workplace/A_pretrain_models/all_MiniLM_L6_v2')
    corpus_embeddings = encoder.encode(corpus)
    write_pkl(f'{root_path}/corpus_embeddings_{mode}.pkl', corpus_embeddings)
    exit()
else:
    corpus_embeddings=read_pkl(f'{root_path}/corpus_embeddings_{mode}.pkl') 
# Perform kmean clustering
clustering_model = KMeans(n_clusters=num_clusters, random_state=1234)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]

for pred, oneline in zip(cluster_assignment, dataset):
    oneline['pred']=int(pred)

dist = clustering_model.transform(corpus_embeddings)
clustered_dists = [[] for i in range(num_clusters)]
clustered_idx = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append((corpus[sentence_id], float(dist[sentence_id][cluster_id])))

clustered_sentences=[sorted(one_cluster, key=lambda x:x[1]) for one_cluster in clustered_sentences]
need_save={}
for idx,one in enumerate(clustered_sentences):
    need_save[f'cluster {idx} label']=''
    need_save[f'cluster {idx}']=one[:3]
write_json(f'{root_path}/clustered_center_{mode}.json', need_save)
write_json(f'{root_path}/result_kmeans_{mode}.json', dataset)

y_km = clustering_model.fit_predict(corpus_embeddings)
pca_model = PCA(n_components=2, random_state=1234)
transformed = pca_model.fit_transform(corpus_embeddings)
centers = pca_model.transform(clustering_model.cluster_centers_)

plt.scatter(x=transformed[:, 0], y=transformed[:, 1], c=y_km, s=50, cmap=plt.cm.Paired, alpha=0.4)
plt.scatter(centers[:, 0],centers[:, 1],
        s=250, marker='*', label='centroids',
        edgecolor='black',
    c=np.arange(0,num_clusters),cmap=plt.cm.Paired,)
plt.xticks([])
plt.yticks([])
plt.savefig(f'{root_path}/result_kmeans_{mode}.png', dpi=600)
plt.clf()