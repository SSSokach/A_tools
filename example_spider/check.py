#!/usr/bin/env python
# encoding: utf-8

import requests
from lxml import etree
import time
from pathlib import Path
import multiprocessing 
from tqdm import tqdm
from glob import glob

wav_list=glob('/data/home/shilongwang/workplace/SeaSound/file/*/*.wav')
print(len(wav_list))