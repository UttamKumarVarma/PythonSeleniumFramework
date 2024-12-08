import pytest
from Pytest.BaseClass import BaseClass

class TestSample(BaseClass):
    def test_useLoggers(self):
        log= self.getLogger()
        log.error("Chepalenu")