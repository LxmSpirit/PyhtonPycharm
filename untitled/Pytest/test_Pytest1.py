#coding=utf-8
'''
xfail
功能测试尚未实施或尚未修复的错误，
当测试通过时尽管预计会失败（标记为pytest.mark.xfail）
它是一个xpass，将在测试摘要中报告
即期望测试由于某种情况而就应该失败
'''

import pytest

class Test_Pytest():

    def test_one(self,):
        print('----start----')
        pytest.xfail(reason='该功能尚未完成')
        print('test_one方法执行')
        assert 1==1

    def test_two(self):
        print('test_two方法执行')
        assert 'o' in 'love'

    def test_three(self):
        print('test_three方法执行')
        assert 3-2==1

if __name__=='__main__':
    pytest.main(['-s','-r','test_Pytest1.py','test_Pytest1.py'])