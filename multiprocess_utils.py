from multiprocessing import Pool
import time


def multi_process(func, datalist, worker_num=4):
    with Pool(worker_num) as pool:
        output = []
        for line in pool.imap(func, datalist):
            output.append(line)
    return output
