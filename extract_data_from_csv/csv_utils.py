import csv
import random
import json
random.seed(1)
def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)

def read_csv(path):
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # csv_reader = csv.DictReader(csv_file)
        
        # 跳过标题行
        header_row=next(csv_reader)
        
        data=[]
        for line in csv_reader:
            data.append(line[0])
    return data


data = [
    {'id':1,'name':'dog',"age":18},
    {'id':2,'name':'cat',"age":19},
    {'id':3,'name':'dog',"age":20},
]
def write_csv(path,data):
    with open(path, 'a') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=['id','name','age'])
        writer.writeheader() # 将字段写入csv格式文件首行
        for line in data:
            writer.writerow(line)


        # writer = csv.writer(csv_file)
        # writer.writerow(['anger','anticipation','disgust','fear','joy','love','optimism','pessimism','sadness','surprise','trust'])
        # for line in merge_predict:
        #     writer.writerow(line)

    
