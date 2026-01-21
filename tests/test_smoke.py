def test_open_main_page(page):
    page.goto("https://the-internet.herokuapp.com/")
    assert "The Internet" in page.title()
