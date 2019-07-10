import numpy as np
import pandas as pd 
import re
import jieba
import csv

def preprocessing(path):
    dataset = pd.read_csv(path)
    #X是酒店评价
    X = dataset.iloc[ : , 1].values
    # print(X)
    #Y是评价的正负面标记信息
    Y = dataset.iloc[ : , 0].values
    #正则标点
    r = '[\s+\!\/_,$%^*(+\"\')]+|[:：+——()?【】“”！，。？、~@#￥%……&*（）]+'
    results = []
    for line in X.astype(str):
        line = re.sub(r,'',''.join(line))
        line = list(jieba.cut(line))
        results.append(line)
    print(results)
    return results,Y

x,y = preprocessing('F:/rachel/WeiboCrawler/labelled.csv')

with open('fenci.csv', 'w', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['tokenization'])
 
with open('fenci.csv', 'a+', encoding="utf-8") as file:
    w = csv.writer(file)
    for i in range(0,len(x)):
        # print(x[i])
        w.writerow([x[i]])