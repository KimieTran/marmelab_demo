from PageObjectLibrary import PageObject
import re
from common import *

from libs.common import click_element_using_mouse_event, input_text_with_retry


class Posters(PageObject):
    IS_DYNAMIC = True
    PAGE_URL = "/react-admin-demo/#/products"

    _locators = {
        "posters": '//.RaMenuItemLink-active.css-18x74ig > div > svg > path//',
        "search_box": '//#q//',
        "third_poster": '//div.MuiImageListItemBar-title.css-1w4d4gp//',
    }

    def _is_current_page(self):
        location = self.se2lib.get_location()
        templateStr = '.*' + self.PAGE_URL.replace('%s', '.*') + '$'
        regexmatch = ''
        for character in templateStr[2:-3]:
            if re.match(r'[[\]()/*+?,\\^$|#\\|]', character):
                regexmatch += '\\' + character
            else:
                regexmatch += character
        template = re.compile(r'%s' % '.*'+regexmatch+'.*$')
        if template.match(location) is None:
            message = "Expected location to end with " + \
                      templateStr + " but it did not"
            raise Exception(message)
        return True

    def wait_for_posters_appear(self, timeout=2):
        """
            Wait for posters appear!
        """
        self.se2lib.wait_until_element_is_visible(self.locator.posters, timeout)

    def wait_for_3rd_poster_appears(self, timeout=2):
        """
            Wait for 3rd poster appears!
        """
        self.se2lib.wait_until_element_is_visible(self.locator.third_poster, timeout)

    def click_posters(self, wait_refresh='true'):
        """Click the posters at the left menu"""
        if wait_refresh=='true':
            with self.wait_for_posters_appear():
                click_element_using_mouse_event(self.locator.posters)
            self.se2lib.wait_until_page_does_not_contain_element(self.locator.poster_appear, timeout=120)
        else:
            click_element_using_mouse_event(self.locator.posters)

    def click_the_search_box(self, wait_refresh='true'):
        """Click the search box"""
        if wait_refresh == 'true':
            with self._wait_for_page_refresh():
                click_element_using_mouse_event(self.locator.search_box)
            self.se2lib.wait_until_page_does_not_contain_element(self.locator.process_popup, timeout=120)
        else:
            click_element_using_mouse_event(self.locator.search_box)

    def enter_3rd_poster(self, search_box):
        """Type the given text into the search box """
        input_text_with_retry(self.locator.search_box, search_box)