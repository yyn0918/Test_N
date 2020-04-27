from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_Addcontact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555  device'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    # def teardown(self):
    # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()

    @pytest.mark.parametrize("username,gender,phonenum", [
        ("测试name1", "男", "13811000001"),
        ("测试name2", "女", "13632580002"),
        ("测试name3", "男", "13833330003")
    ])
    @pytest.mark.skip
    def test_addcontact(self, username, gender, phonenum):
        # 进入到通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找 添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        # 手动添加
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c56").click()
        sleep(2)
        # 验证 添加联系人页面
        current_art = self.driver.current_activity
        assert ".contact.controller.ContactAddActivity" in current_art

        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(
            username)
        # 选择性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/ate']").click()
        sleep(2)
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # 输入电话号码
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)
        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        # assert "添加成功" in self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        sleep(3)

    def test_delcontact(self):
        username = "测试name"
        del_ele = self.driver.find_elements(MobileBy.XPATH, "//*[contains(@text, '" + username + "')]")
        while len(del_ele) != 0:
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '" + username + "')]").click()
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq0").click()
            # 点击【编辑成员】
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/axr").click()
            # 点击【删除成员】
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/drk").click()
            # 点击【确定】
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b89").click()
            sleep(5)
            del_ele = self.driver.find_elements(MobileBy.XPATH, "//*[contains(@text, '" + username + "')]")
        else:
            print("测试用户已全部删除")
