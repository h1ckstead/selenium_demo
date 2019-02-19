from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    CATALOGUE_ITEM = "//*[@id='Catalog']//span[text()='{}']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_catalogue_element_by_name(self, name):
        """

        :param name:
        :return:
        """
        return self.get_element((By.XPATH, self.CATALOGUE_ITEM.format(name)))

    def hover_and_click(self, hover_element, click_element_name):
        """
        Method for hovering over one element and clicking on another element

        :param hover_element: selenium WebElement instance
        :param click_element_name: str
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element)
        click_element = self.get_catalogue_element_by_name(click_element_name)
        actions.click(click_element)
        actions.perform()
