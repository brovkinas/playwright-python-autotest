from pages.base_page import BasePage


class MainPage(BasePage):
    URL = '/'

    def open(self):
        super().open(self.URL)

    def should_have_title(self):
        assert 'The Internet' in self.page.title()