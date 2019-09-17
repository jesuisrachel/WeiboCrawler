from selenium import webdriver
import time
import re

#Chrome webdriver 
driver = webdriver.Chrome("C:/Users/Rachel/AppData/Local/Google/Chrome/Application/chromedriver.exe")


#Weibo login
def loginWeibo(username, password):
    driver.get("https://passport.weibo.cn/signin/login")
    time.sleep(3)

    driver.find_element_by_id("input_nick_name").send_keys(username)
    driver.find_element_by_id("loginPassword").send_keys(password)
    driver.find_element_by_id("loginAction").click()

    time.sleep(3)
    #driver.find_element_by_id("").click()
    cookies = driver.get_cookies()
    cookie_list = []
    for dict in cookies:
        cookie = dict['name'] + '=' + dict['value']
        cookie_list.append(cookie)
    cookie = ';'.join(cookie_list)#将cookie_list中的元素用分号拼接成一个字符串
    print(cookie)

def targetInfo(userId):
    driver.get('http://weibo.com/' + userId)
    #用户信息
    print('*****************************')
    print('userInformation')
    time.sleep(5)
    strName = driver.find_element_by_xpath("//h1[@class='username']")
    strlist = strName.text.split(' ')
    nickname = strlist[0]
    print('nickname:' + nickname)
    print('******************************')
    strCnt = driver.find_element_by_xpath('//div[@class="WB_innerwrap"]')
    pattern = r"\d+\.?\d*"
    cntArr = re.findall(pattern,strCnt.text)
    print(strCnt.text)
    print('following:' + str(cntArr[0]) + '\n')
    print('follower:' + str(cntArr[1]) + '\n')
    print('weiboNum:' + str(cntArr[2]) + '\n')

    #将用户信息写到文件里
    '''with open('userinfo.txt', 'w', encoding = 'gb18030')as file:
        file.write("userID:" + userId + '\r\n')
        file.write("nickname:" + nickname + '\r\n')
        file.write("weiboNum:" + str(cntArr[0]) + '\r\n')
        file.write("following:" + str(cntArr[1]) + '\r\n')
        file.write("follower:" + str(cntArr[2]) + '\r\n')'''

def weiboContent(userId):
    pageList = driver.find_element_by_xpath('//div[@class="WB_text W_f14"]')
    print(pageList.text)

def weiboURL(url):
    driver.get(url)
    title = driver.find_element_by_xpath('//div[@id="precontent"]/header/h1')
    content=driver.find_element_by_xpath('//div[@class="content"]')
    print(content.text)
    with open('test.txt', 'w', encoding="utf-8") as file:
        file.write("标题："+ title.text + '\r\n')
        file.write("内容："+ content.text + '\r\n')

if __name__ == '__main__':
    username = "2974689013@qq.com"
    password = "19960202"
    userId = "5601629229"
    #loginWeibo(username, password)#无需登录也可查看微博
    #targetInfo(userId)
    #weiboContent(userId)
    search_url = 'https://www.msn.cn/zh-cn/entertainment/entertainmentnews/刘强东案女主爆照%ef%bc%8c比奶茶怎么样%ef%bc%9f/ar-BBW64ga?ocid=spartanntp'
    weiboURL(search_url)
    
