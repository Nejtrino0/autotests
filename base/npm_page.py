from webium import BasePage
from webium.wait import wait

from locators.locators import NPMPageLocators


class NPMPage(BasePage, NPMPageLocators):
    def __init__(self, driver, url):
        super().__init__(driver=driver, url=url)
        self.open()

    def fill_search_input(self, *args):
        """
        :param args:
        :return:
        """
        self.search_input.send_keys(*args)

    def click_search_button(self):
        """
        :return:
        """
        wait(
            lambda: self.search_button.click() is None,
            waiting_for='button to be clickable'
        )

    def get_result_list(self, text):
        """
        :param text:
        :return:
        """
        wait(
            lambda: self.result_list,
            waiting_for='until search results are loaded'
        )
        return list(
            filter(
                lambda element: text in element.__getattribute__('text'),
                self.result_list
            )
        )
