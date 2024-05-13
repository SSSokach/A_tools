import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def load_jsonline(path):
    with open(path, "r", encoding="utf-8") as f:
        result = []
        for line_s in f:
            line = json.loads(line_s)
            result.append(line)
    return result


def write_jsonline(path, data):
    with open(path, "w", encoding="utf-8") as f:
        for line in data:
            line_s = json.dumps(line, ensure_ascii=False)
            f.write(line_s)
            f.write("\n")


import pickle


def load_pkl(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


def write_pkl(filename, obj):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)


import csv


def load_csv(path, use_dict=True):
    with open(path, "r") as csv_file:
        if use_dict == True:
            csv_reader = csv.DictReader(csv_file)
        else:
            csv_reader = csv.reader(csv_file)
            header_row = next(csv_reader)
        data = []
        for line in csv_reader:
            data.append(line)
    return data


def write_csv(path, data, fieldnames, use_dict=True):
    """
    fieldnames=['id','name','age']
    """
    with open(path, "w") as csv_file:
        if use_dict:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()  # 将字段写入csv格式文件首行
            for line in data:
                writer.writerow(line)
        else:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            for line in data:
                writer.writerow(line)
