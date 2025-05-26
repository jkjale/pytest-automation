from pages.home_page import HomePage

def test_homepage_title(driver):
    page = HomePage(driver)
    page.load()
    assert "Target" in page.get_title()
