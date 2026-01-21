class BasePage():
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, url: str = ''):
        self.page.goto(f'{self.base_url}{url}')
