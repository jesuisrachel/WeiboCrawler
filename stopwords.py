import pandas as pd

stopwords = pd.read_csv(r"F:\rachel\WeiboCrawler\chinese_stopwords.csv", encoding="utf-8")

for stopword in stopwords:
    print(stopword)