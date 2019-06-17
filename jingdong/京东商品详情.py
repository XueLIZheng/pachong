from selenium import webdriver
import time, re,datetime
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import multiprocessing
import pymysql

reges1 = re.compile('\d+')
reges = re.compile('//item.jd.com/\d+.html')
rege=re.compile('[a-zA-z]+://[^\s]*')
rege_detail_content = re.compile('//img\S*jpg')
rege_color1 = re.compile('<i>\S*</i>')
rege_color2 = re.compile('[\u4e00-\u9fa5]')


def start_urls():
    with open(r'D:\dataDemo\pachong\新建文件夹\5.txt', 'r', encoding='utf-8')as f:
        a = f.read()
        pass
    aa = rege.findall(a)
    for x in set(aa):
        get_data(x)
    pass


def get_data(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.get(url)
    # 模拟向下滑动滚动条
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    try:
        soup = BeautifulSoup(driver.page_source)
        # 商品编号
        number1 = reges1.findall(url)[0]
        # 标题
        title = [x.text.strip()  for x in soup.select('.sku-name')][0]
        print(title)
        # 类别
        html_type1 = soup.select('body > #crumb-wrap > .w > div > div > a')[0].text
        html_type2 = soup.select('body > #crumb-wrap > .w > div > div > a')[1].text
        html_type3 = soup.select('body > #crumb-wrap > .w > div > div > a')[2].text
        print(html_type1,html_type2,html_type3)

        '''
        html_type1 =[z1.text for z1 in [y1 for y1 in [x1 for x1 in soup.select('.w')[2]][1]][1]][0]
        # print(html_type1)
        # 类别2
        html_type2 =[z2.text for z2 in [y2 for y2 in [x2 for x2 in soup.select('.w')[2]][1]][5]][0]
        # print(html_type2)
        # 类别3
        html_type3 = [z3.text for z3 in [y3 for y3 in [x3 for x3 in soup.select('.w')[2]][1]][9]][0]
        # print(html_type3)
        '''
        # 样品图
        img_urls = ''
        for x in soup.select('.lh > li >img'):
            img_urls += x['src']
        # print(img_urls)
        # 颜色
        color = ''
        if soup.select('#choose-attrs'):
            for x in  soup.select('#choose-attrs'):
                for y,z in zip(rege_color1.findall(str(x)),rege_detail_content.findall(str(x))):
                    color += y+ ' '+z
        # print(color)
        # 价格
        if soup.select('.dd > span >span'):
            price = [x.text for x in soup.select('.dd > span >span')][1]
        else:
            price = ''
        # print(price)
        # 商品介绍
        content = ''
        for x in soup.select('.p-parameter > ul'):
            content += x.text
        # print(content)
        # 规格和包装
        sp1 = soup.select('.Ptable-item > dl > dl >dt')
        sp2 = soup.select('.Ptable-item > dl > dl >dd')
        dict1 = ''
        for x,y in zip(sp1,sp2):
            # print('规格和包装')
            # print()
            dict1 += ' '+x.text+':'+y.text
            pass
        # print(dict1)
        # 包装清单
        package_list =[x.text for x in soup.select('.package-list > p')][0]
        # print(package_list)
        # 商品详情
        content_img = ''
        if soup.select('#J-detail-content'):
            aaa = soup.select('#J-detail-content')
            for x in aaa:
                if len(x)>0:
                    bbb = rege_detail_content.findall(str(x))
                    for y in bbb:
                        content_img += y
        # print(content_img)
        mysql(number1,title,html_type1,html_type2,html_type3, img_urls,color, price,content,dict1,package_list,content_img)
        time.sleep(2)
        driver.quit()
    except Exception as ex:
        error1 = str(ex)
        time1 = str(datetime.datetime.now())
        with open(r"D:\dataDemo\pachong\新建文件夹\cuowu.txt", mode="a+", encoding='utf-8') as f:
            f.write(time1+'     '+url+'   异常: '+error1+'\n')
            pass
        driver.quit()
    pass


class down_mysql:
    def __init__(self, number1,title,html_type1,html_type2,html_type3, img_urls,color, price,content,dict1,package_list,content_img):
        self.number1 = number1
        self.title = title
        self.html_type1 = html_type1
        self.html_type2 = html_type2
        self.html_type3 = html_type3
        self.img_urls = img_urls
        self.color = color
        self.price = price
        self.content = content
        self.dict1 = dict1
        self.package_list = package_list
        self.content_img = content_img
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
        sql = "insert into shangpinxiangqing(number1,title,html_type1,html_type2,html_type3,img_urls,color,price,content,dict1,package_list,content_img) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql, (self.number1, self.title,self.html_type1,self.html_type2,self.html_type3, self.img_urls,self.color, self.price, self.content, self.dict1, self.package_list,self.content_img))
            self.connect.commit()
            print('数据插入成功')
        except:
            print('数据插入错误')


# 新建对象，然后将数据传入类中
def mysql(number1,title,html_type1,html_type2,html_type3, img_urls, color,price,content,dict1,package_list,content_img):
    down = down_mysql(number1,title,html_type1,html_type2,html_type3, img_urls,color, price,content,dict1,package_list,content_img)
    down.save_mysql()


if __name__ == '__main__':
    # get_data('https://item.jd.com/48458880024.html')
    start_urls()