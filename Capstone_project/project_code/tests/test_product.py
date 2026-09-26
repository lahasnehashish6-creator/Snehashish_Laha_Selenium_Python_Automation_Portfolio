from pages.home_page import HomePage


def test_product_search(driver):

    home_page = HomePage(driver)

    home_page.search_product("MacBook")

    assert "MacBook" in driver.page_source