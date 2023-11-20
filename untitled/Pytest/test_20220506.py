# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:46
# @Author  : zzt

import allure
import pytest

@allure.feature('这里是一级标签')
class TestAllure():

    @allure.title("用例标题0")
    @allure.story("这里是第一个二级标签")
    @pytest.mark.parametrize('param', ['青铜', '白银', '黄金'])
    def test_0(self, param):
        allure.attach('附件内容是： '+param, '我是附件名', allure.attachment_type.TEXT)

    @allure.title("用例标题1")
    @allure.story("这里是第二个二级标签")
    def test_1(self):
        allure.attach.file(r'E:\Myproject\pytest-allure\test\test_1.jpg', '我是附件截图的名字', attachment_type=allure.attachment_type.JPG)

    @allure.title("用例标题2")
    @allure.story("这里是第三个二级标签")
    @allure.severity(allure.severity_level.NORMAL)
    def test_2(self):
        pass