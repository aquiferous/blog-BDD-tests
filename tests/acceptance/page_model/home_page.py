from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property # to access without brackets
    def url(self):
        return super(HomePage, self).url + '/'

        # * deconstructs the tuple and passes as 2 arguments

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)
