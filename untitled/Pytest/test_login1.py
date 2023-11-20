#coding=utf-8

import pytest
import time

@pytest.mark.usefixtures('open_url')
class Test_Login():

    #pytestmark = pytest.mark.login #整个Test_Login类里面，所有测试用例都有login标签
    #@pytest.mark.smoke
    def test_login_success(self,open_url):

        print("test_login_success")
        assert 1 == 1


if __name__=='__main__':
    pytest.main(['-s','test_login1.py'])