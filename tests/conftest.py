import os

import pytest
import yaml
from selenium import webdriver

from pages.main_page import MainPage
from pages.section_page import SectionPage

PROJECT_DIR = os.path.dirname(__file__).rsplit("/", 1)[0]


@pytest.fixture(scope="module")
def test_config():
    with open(os.path.join(PROJECT_DIR, "testconfig.yaml"), "r", encoding='utf8') as config:
        full_data = yaml.load(config)
    return full_data


@pytest.fixture(scope="module")
def urls(test_config):
    return test_config.get("urls")


@pytest.fixture(scope="module")
def expected_page_titles(test_config):
    return test_config.get("page_titles")


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path=os.environ.get("webdriver_path"))
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture
def main_page(driver, urls):
    main_page = MainPage(driver)
    main_page.driver.get(urls.get("base_url"))
    return main_page


@pytest.fixture
def notebooks_page(driver, urls):
    notebooks_page = SectionPage(driver)
    notebooks_page.driver.get(urls.get("base_url") + urls.get("notebooks_url"))
    return notebooks_page
