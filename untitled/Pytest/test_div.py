#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pytest文件和函数命名规则
#pytest文件必须以test开头或者_test结尾，否则在pytest解释器运行时，文件不能够被收集
#pytest文件中测试类命名时，必须用Test开头
#Pytest文件中方法与函数命名必须要用test_开头

#pytest的框架结构
'''
模块级（setup_module/teardown_module）模块始末，全局的（优先级最高）
函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
类级（setup_class/teardown_class）只在类中前后运行一次（在类中）
方法级（setup_method/teardown_method)开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
'''

'''
def div(a,b):
    return a/b

class TestDiv:
    def test_div(self0):
        assert 1==div(1,1)
'''

# 模块级别
def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源消毁：teardown module")


def test_case1():
    print("case1")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源消毁：teardown function")


class TestDemo:

    #  执行类 前后分别执行setup_class  teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup, teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")


class TestDemo1:

    #  执行类 前后分别执行setup_class  teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup, teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
