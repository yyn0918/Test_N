from appium import webdriver
"""
    1.打开企业微信（提前登录）
    2.进入通讯录
    3.点击搜索按钮
    4.输入 已存在的联系人姓名, 例如“aa”，
    5.点击联系人，进入聊天页面
    6.输入“测试code”
    7.点击发送
    8.退出应用
"""

class Test_Wework():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555  device'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['dontStopAppOnReset']=True
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()

    # self.driver.quit()

    def test_sendmsg(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys("user1")
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView").click()
        self.driver.find_element_by_id("com.tencent.wework:id/aam").click()
        self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys("测试code")
        self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()
        self.driver.find_element_by_id("com.tencent.wework:id/dtg").click()
