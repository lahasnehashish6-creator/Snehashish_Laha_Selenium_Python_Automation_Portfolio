from pages.login_page import LoginPage
from utils.csv_reader import read_test_data
from utils.screenshot import take_screenshot


def test_invalid_login(driver):

    data = read_test_data()[0]

    login_page = LoginPage(driver)

    try:
        # Open login page
        driver.get(
            "https://tutorialsninja.com/demo/index.php?route=account/login"
        )

        # Perform login
        login_page.login(
            data["email"],
            data["password"]
        )

        # Get warning message
        warning = login_page.get_warning()

        # Verify warning
        assert "Warning" in warning

    except Exception:
        take_screenshot(driver, "login_failure")
        raise