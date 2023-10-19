import json
import os
from pycocoevalcap.eval import COCOEvalCap
def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)

def load_jsonline(path):
    with open(path, 'r', encoding='utf-8') as f:
        result=[]
        for line_s in f:
            line=json.loads(line_s)
            result.append(line)
    return result

def write_jsonline(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        for line in data:
            line_s=json.dumps(line, ensure_ascii=False)
            f.write(line_s)
            f.write('\n')

path_list=[
    'baichuan_lora_7b_5epo_4lorar',
    'baichuan-chat_lora_7b_5epo_4lorar',
]

new_result=[]
Metric=COCOEvalCap()
for path in path_list:
    data = load_json(f'/home/shilongwang/workplace/hfl_generate_model/panda_chat/generate_result/{path}.json')
    cands = [line['predict'] for line in data]
    refs = [line['target'] for line in data]
    one_result={'model_name':path}
    one_result.update(Metric.evaluate(cands, refs))
    new_result.append(one_result)
result=new_result
from tabulate import tabulate
need_metric=['model_name','Bleu_1','Bleu_2','Bleu_3','Bleu_4','ROUGE_L','METEOR','CIDEr', 'Dist_1','Dist_2']
table_header=['-'] + need_metric[1:]
info=[]
for one_result in result:
    one_line=[]
    for one_metric_name in need_metric:
        one_line.append(one_result[one_metric_name])
    info.append(one_line)
print(tabulate(info, headers=table_header, tablefmt='fancy_grid'))