import json
import random
random.seed(1234)
def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

dataset=load_json('raw_data/dataset.json')











train_ratio=0.7
valid_ratio=0.15
train_offset = int(len(dataset) * train_ratio)
valid_offset = int(len(dataset) * (train_ratio+valid_ratio))

random.shuffle(dataset)

dataset_train=dataset[:train_offset]
dataset_valid=dataset[train_offset:valid_offset]
dataset_test=dataset[valid_offset:]

write_json('./dataset_train.json',dataset_train)
write_json('./dataset_valid.json',dataset_valid)
write_json('./dataset_test.json',dataset_test)

