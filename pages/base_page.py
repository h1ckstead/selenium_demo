from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    HEADER_LOGO = (By.XPATH, "//*[@id='Layer_1']")

    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    def get_element(self, locator):
        """
        Searches for an element by a given locator

        :param locator: set, is used to find element
        :return: selenium WebElement instance
        """
        return WebDriverWait(self.driver, 5).until(presence_of_element_located(locator))
