import allure  # noqa
from .base_element import BaseElement


class Checkbox(BaseElement):

    def check(self):
        with allure.step(f"Set checkbox '{self.name}'"):
            self._locator.check()

    def uncheck(self):
        with allure.step(f"Unset checkbox '{self.name}'"):
            self._locator.uncheck()
