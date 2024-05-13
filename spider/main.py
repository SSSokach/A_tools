#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: xag
@license: Apache Licence
@contact: xinganguo@gmail.com
@site: http://www.xingag.top
@software: PyCharm
@file: 4.dytt.py
@time: 2018/9/16 18:46
@description：爬电影天堂【 lxml + xpath + requests】【2018新片精品，包含更多】
"""

import requests
from lxml import etree
import time
from pathlib import Path
import multiprocessing 
from tqdm import tqdm

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}

def get_html_form_urls(url):
    response = requests.get(url, headers=HEADERS)
    html_element = etree.HTML(response.text)
    return html_element

def download_file(url,save_path):
    req = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(req.content)

# def request_file(url):


def spider():
    """
    爬虫的入口
    :return:
    """
    # base_url = 'https://cis.whoi.edu/science/B/whalesounds/'

    # html_element = get_html_form_urls(base_url+'index.cfm')

    # detail_urls = html_element.xpath('//div[@class="row"]/div[@class="large-3 columns"]')


    # animal_classes_url={}
    # for one_element in detail_urls[:31]:
    #     one_url_element=one_element.xpath('./a')[0]
    #     url=one_url_element.attrib['href']
    #     name=one_url_element.xpath('./div/h3')[0].text
    #     animal_classes_url[name]=base_url+url
    # print(animal_classes_url)


    animal_classes_url={'Atlantic Spotted Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD15F', 'Bearded Seal': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=CC2A', 'Beluga, White Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BB1A', 'Bottlenose Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD19D', 'Bowhead Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=AA1A', 'Clymene Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD15B', 'Common Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD3B', 'False Killer Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BE9A', 'Fin, Finback Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=AC1F', "Fraser's Dolphin": 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD5A', "Grampus, Risso's Dolphin": 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD4A', 'Harp Seal': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=CC12G', 'Humpback Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=AC2A', 'Killer Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BE7A', 'Leopard Seal': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=CC4A', 'Long-Finned Pilot Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BE3C', 'Melon Headed Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD10A', 'Minke Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=AC1A', 'Narwhal': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BB2A', 'Northern Right Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=AA3A', 'Pantropical Spotted Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD15A', 'Ross Seal': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=CC14A', 'Rough-Toothed Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD17A', 'Short-Finned (Pacific) Pilot Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BE3D', 'Southern Right Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=AA3B', 'Sperm Whale': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BA2A', 'Spinner Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD15L', 'Striped Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD15C', 'Walrus': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=CB1A', 'Weddell Seal': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=CC5A', 'White-beaked Dolphin': 'https://cis.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD6B'}

    save_root_path='/data/home/shilongwang/workplace/SeaSound/file'
    download_list=[]
    for name,url in animal_classes_url.items():
        name=name.split(',')[-1].strip().replace(' ','_')
        Path(f'{save_root_path}/{name}').mkdir(exist_ok=True,parents=True)

        html_element=get_html_form_urls(url)
        detail_urls = html_element.xpath('//table//tr/td/a[@target="_blank"]')
        for i,one_element in enumerate(tqdm(detail_urls)):
            one_url=one_element.attrib['href']
            one_url='https://cis.whoi.edu'+one_url
            download_list.append([one_url,f'{save_root_path}/{name}/{i}.wav'])
            # download_file(one_url,f'{save_root_path}/{name}/{i}.wav')
    print(len(download_list))
    # pool = multiprocessing.Pool(processes = 5)
    # for _ in pool.map(download_file, tqdm(download_list)):
    #     pass

        

if __name__ == '__main__':
    spider()