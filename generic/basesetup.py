import pytest
from selenium.webdriver import Chrome


class BaseSetup:

    @pytest.fixture(autouse=True)
    def precondition(self):
        self.driver = Chrome()

    @pytest.fixture(autouse=True)
    def postcondtion(self):
        yield
        self.driver.quit()
