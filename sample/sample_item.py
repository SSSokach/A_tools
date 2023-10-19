
import random
random.seed(123)
import json
import re
import sys
sys.path.append('/home/shilongwang/workplace/A_tools')
from utils import *

data=load_json('/home/shilongwang/workplace/hfl_generate_model/panda_chat/generate_result/baichuan-chat_lora_7b_5epo_4lorar.json')

sample_data=random.sample(data, 140)

write_json('/home/shilongwang/workplace/A_tools/sample/baichuan-chat_lora_7b_5epo_4lorar_sample140.json',sample_data)
