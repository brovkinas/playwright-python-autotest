import allure  # noqa
from playwright.sync_api import Locator, expect


class BaseElement:

    def __init__(self, locator: Locator, name: str, is_secret: bool = False):
        self._locator = locator
        self.name = name
        self.is_secret = is_secret

    # =============================
    # ========== Actions ==========
    def click(self):
        with allure.step(f"Click: '{self.name}'"):
            self._locator.click()

    def hover(self):
        with allure.step(f"Hover: '{self.name}'"):
            self._locator.hover()

    def double_click(self):
        with allure.step(f"Double click: '{self.name}'"):
            self._locator.dblclick()

    def get_text(self) -> str:
        with allure.step(f"Get text from '{self.name}'"):
            return self._locator.inner_text()

    def select_option(self, option: str):
        with allure.step(f"For element '{self.name}' select '{option}'"):
            return self._locator.select_option(option)

    # =============================
    # ========= Assertions ========
    def should_be_visible(self):
        with allure.step(f"Element '{self.name}' should be visible"):
            expect(self._locator).to_be_visible()

    def should_not_be_visible(self):
        with allure.step(f"Element '{self.name}' should NOT be visible"):
            expect(self._locator).not_to_be_visible()

    def should_be_enabled(self):
        with allure.step(f"Element '{self.name}' should be enabled"):
            expect(self._locator).to_be_enabled()

    def should_not_be_enabled(self):
        with allure.step(f"Element '{self.name}' should NOT be enabled"):
            expect(self._locator).not_to_be_enabled()

    def should_contain_text(self, text: str):
        with allure.step(f"'{self.name}' should contain text: '{text}'"):
            expect(self._locator).to_contain_text(text)

    def should_not_contain_text(self, text: str):
        with allure.step(f"'{self.name}' should NOT contain text: '{text}'"):
            expect(self._locator).to_not_contain_text(text)

    def should_have_exact_text(self, text: str):
        with allure.step(f"Element '{self.name}' should have exact text: '{text}'"):
            expect(self._locator).to_have_text(text)

    def should_not_have_exact_text(self, text: str):
        with allure.step(f"Element '{self.name}' should NOT have exact text: '{text}'"):
            expect(self._locator).to_have_text(text)
