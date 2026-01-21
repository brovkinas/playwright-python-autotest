def test_open_main_page(page, base_url):
    page.goto(base_url)
    assert "The Internet" in page.title()
