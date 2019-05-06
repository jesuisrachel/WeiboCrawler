import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode

#request url:https://m.weibo.cn/api/container/getIndex?containerid=1076035601629229
host =  'm.weibo.cn'
base_url = 'https://%s/api/container/getIndex?' %host
user_agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0'
userId = 1005055601629229

headers = {
    'Host': host,
    'Referer': 'https://m.weibo.cn/u/1005055601629229',
    'User-Agent': user_agent
}

def get_data_by_page(page):
    params={
        "containerid": 1076035601629229,
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
    items = json.get('data').get('cards')
    for item in items:
        item = item.get('mblog')
        if item:
            data = {
                'text': pq(item.get("text")).text(),  # 仅提取内容中的文本
                'attitudes': item.get('attitudes_count'),
                'comments': item.get('comments_count'),
                'reposts': item.get('reposts_count')
            }
            yield data

if __name__ == '__main__':
    for page in range(2, 9):  # 抓取前十页的数据
        json = get_data_by_page(page)
        results = parse_page(json)
        for result in results:
            print(result)



