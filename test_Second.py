def test_2(browser):
    browser.get('https://the-internet.herokuapp.com/context_menu')
    string = "Alibaba"
    assert string in browser.page_source
