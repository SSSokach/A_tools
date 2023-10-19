import json

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('/users10/shilongwang/workplace/pretrained_models/roberta-base')

data=load_json('./mcec_train.json')

for line in data:
    text=line['Text']
    f=tokenizer(text)

    print(text)
    temp=tokenizer.tokenize(text)
    print(temp)
    temp=tokenizer.convert_tokens_to_ids(temp)
    print(temp)
    print(f)
    input()
