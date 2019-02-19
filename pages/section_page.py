from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SectionPage(BasePage):

    MANUFACTURER = "//*[@class='ModelFilter__TipAttr']//label[text()='{}']"
    TOOLTIP_VALUE = (By.XPATH, "//*[@id='count_item']")
    TOOLTIP_SEARCH_BUTTON = (By.XPATH,
                             "//*[@class='ModelFilter__NumModelBtn Page__ActiveButtonBg ModelFilter__GALink']")
    FILTERED_ITEMS_COUNT = (By.XPATH, "//*[@class='PanelSetUp__CountBlockItem']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_manufacturer_element_by_name(self, name):
        """

        :param name:
        :return: selenium WebElement instance
        """
        return self.get_element((By.XPATH, self.MANUFACTURER.format(name)))

    def get_tooltip_value(self):
        """

        :return: selenium WebElement instance
        """
        return self.get_element(self.TOOLTIP_VALUE).text

    def get_filtered_value(self):
        """

        :return:
        """
        raw_value = self.get_element(self.FILTERED_ITEMS_COUNT).text
        numbers = [i for i in raw_value.split() if i.isdigit()]
        return " ".join(numbers)

    def get_tooltip_search_button(self):
        """

        :return: selenium WebElement instance
        """
        return self.get_element(self.TOOLTIP_SEARCH_BUTTON)
