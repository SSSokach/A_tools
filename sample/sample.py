
import random
random.seed(1)
import json
import re


pattern_d="\d+ \d+ \d+"
prog_d= re.compile(pattern_d)
pattern_s="\[.+\]"
prog_s= re.compile(pattern_s)
def reg_replace(s):
    s=prog_d.sub('',s)
    s=prog_s.sub('',s)
    s=s.strip()
    return s

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)

with open('./testWithStrategy_short.tsv', 'r') as f:
    texts=f.readlines()
print(texts[0])
index=random.sample([i for i in range(len(texts))], 30)
data_sample = [texts[i] for i in index]
data_sample = [[i.strip() for i in texts[i].split('EOS')] for i in index]

# 去掉数字，策略
new_data_sample=[]
for d in data_sample:
    temp=[reg_replace(i) for i in d]
    new_data_sample.append({
        'context': temp[:-1],
        'reference': temp[-1],
        'generate_zero':'',
        'generate_few':'',
        'generate_prompt':'',
    })
write_json('./ESConv_test_sample30.json',new_data_sample)
