import pytest
from selenium import webdriver
from utils.config_reader import get_config


@pytest.fixture
def driver():
    config = get_config()

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(config["base_url"])

    yield driver

    driver.quit()