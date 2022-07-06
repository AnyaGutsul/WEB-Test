def test_1(browser):
    browser.get('https://the-internet.herokuapp.com/context_menu')
    string = "Right-click in the box below to see one called 'the-internet'"
    assert string in browser.page_source
