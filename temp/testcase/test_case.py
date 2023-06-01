import time
import pytest
from commom.excel_util import ExcelUtil
from pageobject.a_page import One
from pageobject.b_page import Two


class TestCase:

    @pytest.mark.parametrize("code", ExcelUtil().read_1())
    def test01(self, code):
        t1 = One()
        time.sleep(6)
        t1.enter()
        t1.create(code)
        time.sleep(3)
        t1.edit()

    @pytest.mark.parametrize("history", ExcelUtil().read_2())
    def test02(self, history):
        t2 = Two()
        t2.enter()
        t2.create(history)

