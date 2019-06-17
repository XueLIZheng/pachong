from selenium import webdriver
import time, re, pymysql , os,datetime
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

reges1 = re.compile('\d+')
reges = re.compile('//\S*')
rege=re.compile('[a-zA-z]+://[^\s]*')
page_rege = re.compile('page=\d+')




def get_urls():
    with open(r'D:\dataDemo\untitled1\1.txt', 'r', encoding='utf-8')as f:
        a = f.read()
        pass
    aa = rege.findall(a)
    # print(aa)
    for x in aa:
        print(x)
        get_data(x)

    pass


def get_data(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.get(url)
    try:
        while True:
            time.sleep(1)
            # 模拟向下滑动滚动条
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source)
            # 页数
            html_page = soup.select('#J_topPage > span > b')
            for x in html_page:
                print(x.text)
            html_num = soup.select('.gl-item')
            # print(type(html_num))
            for x in html_num:
                # 商品编号
                num = reges1.findall(x.a['href'])[0]
                # 商品链接
                url = 'https:'+ reges.findall(x.a['href'])[0]
                print(num+'     '+url)
                mysql(num,url)
                pass
            time.sleep(1)
            next_url = driver.find_elements_by_xpath('//a[@class="pn-next"]')
            # print(next_url)
            # 找到翻页的信息,进行点击
            next_url = next_url[0] if len(next_url) > 0 else None
            # print(next_url)
            if next_url == None:
                break
            next_url.click()
            time.sleep(1)
        driver.quit()
    except Exception as ex:
        error1 = str(ex)
        time1=str(datetime.datetime.now())
        with open(r"D:\dataDemo\pachong\fenleicuowu.txt", mode="a+", encoding='utf-8') as f:
            f.write( time1+'  '+ url + '   异常: ' + error1 + '\n')
            pass
        driver.quit()
    pass


class down_mysql:
    def __init__(self, name, urls):
        self.name = name
        self.urls = urls
        self.connect = pymysql.connect(
            host='localhost',
            db='test',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()

    # 保存数据到MySQL中
    def save_mysql(self):
        sql = "insert into shangpinurls0612(`name`,urls) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql, (self.name, self.urls))
            self.connect.commit()
            print('数据插入成功')
        except:
            print('数据插入错误')

# 新建对象，然后将数据传入类中
def mysql(name, urls):
    down = down_mysql(name, urls)
    down.save_mysql()

    '''
    driver.maximize_window()
    #打开浏览器
    driver.get('https://search.jd.com/Search?keyword=鞋&enc=utf-8&page=')
    time.sleep(2)
    # driver.save_screenshot('xueqiu.jpg')  保存快照
    # 模拟向下滑动滚动条
    # for i in range(4):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    #获取加载更多 的标签 模拟点击
    # obj = driver.find_element(By.LINK_TEXT,'加载更多')
    # for j in range(10):
    #     obj.click()
    #     time.sleep(1)
    # #   获取整个页面内容
    # soup = BeautifulSoup(driver.page_source)
    # print(soup)

    print(number1)
    # for x in number1:
        # num = x.find_element_by_xpath('//div[@class="p-img"]/a/@href')
        # print(num)
        # print(x)

   
    # rs = soup.find_all('div',class_= 'home__timeline__item')
    # with open('雪球.csv','w+',encoding='utf-8-sig',newline='')as f :
    #     res = csv.writer(f)
    #     res.writerow(['类型','链接'])
    #     for item in rs:
    #         # autor = item.div.div.a[1].string
    #         title = item.h3.a.string
    #         con = item.p.string
    #         res.writerow([title,con])
    #         # print(autor,title,con)
    #         print('----------ending----------')
    # # 关闭浏览器

 '''
if __name__ == '__main__':
    # get_data('https://www.jd.com/')
    get_urls()