#coding=utf-8

'''
@pytest.mark.xfail标签，
期望用例时失败的，但不会影响测试用例的执行
如果用例执行失败则结果是xfail
如果用例执行成功则结果是xpass
'''

import pytest

class Test_Pytest():

    @pytest.mark.xfail
    def test_one(self):
        print("test_one方法执行")
        assert 1==2

    def test_two(self):
        print('test_two方法执行')
        assert 'o' in 'love'

    def test_three(self):
        print('test-three方法执行')
        assert 3-2==1

if __name__=='__main__':
    pytest.main(['-s','test_PytestXfail'])