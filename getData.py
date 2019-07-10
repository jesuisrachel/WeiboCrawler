import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode
import csv

#request url:https://m.weibo.cn/api/container/getIndex?containerid=1076035601629229
host =  'm.weibo.cn'
base_url = 'https://%s/api/container/getIndex?' %host
user_agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0'
userId = 1005055601629229

headers = {
    'Host': host,
    'Referer': 'https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E5%9E%83%E5%9C%BE%E5%88%86%E7%B1%BB%23&isnewpage=1&luicode=10000011&lfid=100103type%3D38%26q%3D%E5%9E%83%E5%9C%BE%E5%88%86%E7%B1%BB%26t%3D0',
    'User-Agent': user_agent
}

def get_data_by_page(page):
    params={
        "containerid": '231522type=61&q=#垃圾分类#&t=0',
        "isnewpage":1,
        "luicode":10000011,
        "lfid": "100103type=38&q=垃圾分类&t=0",
        "page_type": 'searchall',
        "page": page #为1的时候不传
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)

def parse_page(json):
    data = json.get('data').get('cards')
    for d in data:
        items = d.get('card_group')
        for item in items:
            item = item.get('mblog')
            if item:
                data = {
                    'text': pq(item.get("text")).text().replace('\n',''),  # 仅提取内容中的文本
                    'attitudes': item.get('attitudes_count'),
                    'comments': item.get('comments_count'),
                    'reposts': item.get('reposts_count')
                }
                yield data

def init_csv():
    with open('dataset.csv', 'w', encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(['text','attitudes','comments','reposts'])

def write_in_csv(results):
    print("*******************************************")
    for result in results:
        with open('dataset.csv', 'a+', encoding = 'utf-8') as file:
            w = csv.writer(file)
            w.writerow([result['text'], result['attitudes'], result['comments'], result['reposts']])
            print("####################################################")
        

if __name__ == '__main__':
    init_csv()
    for page in range(1, 9):  # 抓取前十页的数据
        json = get_data_by_page(page)
        try:
            results = parse_page(json)
            for result in results:
                print(result)
            write_in_csv(results)
        except Exception as e:
            print("异常", e)