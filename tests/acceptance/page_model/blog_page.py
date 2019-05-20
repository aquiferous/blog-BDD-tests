from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):
    @property # to access without brackets
    def url(self):
        return super(BlogPage, self).url + '/blog'

        # * deconstructs the tuple and passes as 2 arguments

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)
        # there might be multiple, so this returns a list

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)