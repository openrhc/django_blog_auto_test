from Logger import MyLogger
from selenium import webdriver
import time
from selenium import webdriver
from Logger.MyLogger import Logger

mylogger = Logger(logger='TestMyLog').getlog()

class testBlog(object):
    def  __init__(self):
        self.driver = webdriver.Edge(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')

    def exit(self):
        self.driver.quit()

    def cap(self):
        mylogger.info("开始截图测试")
        try:
            self.driver.get("http://centos/")
            time.sleep(2)
            self.driver.get_screenshot_as_file('home.png')
            self.driver.get("http://centos/detail/?id=1")
            time.sleep(2)
            self.driver.get_screenshot_as_file('details.png')
            mylogger.info("截图成功")
        except BaseException as msg:
            print(msg)

    def login(self):
        mylogger.info("登录测试")
        mylogger.info("正在打开网页")
        self.driver.get("http://centos/login/")

        username = self.driver.find_element_by_id("id_login")
        username.send_keys("18196789181")

        password = self.driver.find_element_by_id("id_password")
        password.send_keys("12345678")

        remember = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[3]/label')
        remember.click()

        self.driver.find_element_by_id("submit_login").click()

    def article(self):
        mylogger.info("写文章测试")
        self.driver.get("http://centos/")
        time.sleep(1)
        isLogin = self.driver.find_element_by_xpath('/html/body/div/nav/div[2]/ul/li/a').text
        if isLogin == '登录':
            self.login()
            self.article()
        self.driver.get("http://centos/writeblog/")
        # 手动添加图片
        input('选择图片zhong...')
        self.driver.find_element_by_id('title').send_keys('自动添加的文章' + str(time.time()))
        self.driver.find_element_by_id('tags').send_keys('python')
        self.driver.find_element_by_id('sumary').send_keys('摘要。。。')
        time.sleep(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath('/html/body').send_keys('自动添加的文章正文')
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()
        self.driver.get("http://centos/")

    def comment(self):
        mylogger.info("评论测试")
        self.driver.get("http://centos/detail/?id=1")
        time.sleep(2)
        isLogin = self.driver.find_element_by_xpath('/html/body/div/nav/div[2]/ul/li/a').text
        if isLogin == '登录':
            self.login()
            self.article()
        for i in range(1):
            time.sleep(2)
            self.driver.switch_to.frame(0)
            content = self.driver.find_element_by_xpath('/html/body')
            content.send_keys('测试评论' + str(i) + ' time:' + str(time.time()))
            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/form/button').click()

    def center(self):
        mylogger.info("个人中心测试")
        self.driver.get("http://centos/")
        time.sleep(2)
        isLogin = self.driver.find_element_by_xpath('/html/body/div/nav/div[2]/ul/li/a').text
        if isLogin == '登录':
            self.login()
            self.center()
        self.driver.get("http://centos/center")
        self.driver.find_element_by_id('desc').send_keys('自动化测试用户的简介')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/form/button').click()

    def register(self):
        mylogger.info("注册测试")
        self.driver.get("http://centos/register/")
        self.driver.find_element_by_id('id_login').send_keys('18196789181')
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[2]/div/input').send_keys('12345678')
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[3]/div/input').send_keys('12345678')
        code = input('输入图片验证码：')
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[4]/div/div/input').send_keys(code)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[5]/div/span').click()
        code = input('输入短信验证码：')
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[5]/div/div/input').send_keys(code)
        self.driver.find_element_by_id('submit_login').click()

test = testBlog()

# test.register()
while True:
    print('1. 测试登录模块         2.测试注册模块')
    print('3. 测试写文章模块       4.测试添加评论模块')
    print('5. 测试个人中心模块      6.截图测试')
    i = input('选择操作：')
    if i == '1':
        test.login()
    elif i == '2':
        test.register()
    elif i == '3':
        test.article()
    elif i == '4':
        test.comment()
    elif i == '5':
        test.center()
    elif i == '6':
        test.cap()
    else:
        test.exit()
        exit()


