# -*- coding: utf-8 -*-

# @File  : test_decorator.py
# @Author: Lomo
# @Site  : lomo.space
# @Date  : 2022/1/16
# @Desc  : 

import pytest

from pkg import decorator_tools


class TestDecoratorTools:

    @pytest.fixture(scope='function')
    def test_deply_func(self):
        @decorator_tools.DelayExecute(3)
        def func_test():
            print('this is a delay func test')

    @decorator_tools.DelayExecute(3)
    def test_delay_3(self):
        print('该函数延迟执行 ...')
        return 'delay 3s '


if __name__ == '__main__':
    pytest.main(['-s', 'test_decorator.py'])
