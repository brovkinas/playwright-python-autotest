import allure  # noqa
from .base_element import BaseElement


class Input(BaseElement):

    def fill(self, value: str):
        with allure.step(f"Fill '{self.name}' with value: '{value}'"):
            self._locator.fill(value)

    def clear(self):
        with allure.step(f"Clear '{self.name}'"):
            self._locator.clear()
