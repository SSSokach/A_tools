import os
import openpyxl
import json

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

file_path='/home/shilongwang/workplace/yky/sentence_keywords/dictionary'
file_name='词表数据_20230928.xlsx'
workbook = openpyxl.load_workbook(os.path.join(file_path,file_name))	# 返回一个workbook数据类型的值
print(workbook.sheetnames)	# 打印Excel表中的所有表

sheet = workbook['Sheet1']  # 获取指定sheet表
print(sheet)
print(sheet.dimensions)

dataset=[]
cell = sheet['A3:D1225']
for i in cell:
    dataset.append(
        {
            'topic':i[0].value,
            'emotion':i[1].value,
            'prompt':i[2].value,
            'dialog':i[3].value
        }
    )
print(len(dataset))

write_json(os.path.join(file_path,'raw_dataset.json'),dataset)

