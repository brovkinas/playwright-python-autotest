def test_open_main_page(main_page):
    main_page.open()
    main_page.should_have_title()
