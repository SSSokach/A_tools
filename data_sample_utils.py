import random

random.seed(1234)


def random_split(data_list, ratio=None, num=None):
    if ratio == None and num == None:
        assert False
    elif ratio == None and num != None:
        if num > len(data_list):
            assert False
    elif ratio != None:
        num = int(ratio * len(data_list))
        
    idx_list = [i for i, _ in enumerate(data_list)]
    random.shuffle(idx_list)
    sample_list = [data_list[i] for i in idx_list[:num]]
    remain_list = [data_list[i] for i in idx_list[num:]]
    return sample_list, remain_list
