import pageobject as pageobject
from PageOcjectLibrary import *
import re
from common import *

from libs.common import input_text_with_retry, click_element_using_mouse_event


class LoginPage(pageobject):
    IS_DYNAMIC = True
    PAGE_URL = "react-admin-demo/#/login"

    _locators = {
        "username": '//#username//',
        "password": '//#password//',
        "signin_btn": '//.css-7roxmj > button//',

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

    def enter_username(self, username):
        """Type the given text into the username field """
        input_text_with_retry(self.locator.username, username)

    def enter_password(self, password):
        """Type the given text into the password field"""
        input_text_with_retry(self.locator.password, password)

    def click_signin_button(self, wait_refresh='true'):
        """Click the signin button, and wait for the page to reload"""
        if wait_refresh == 'true':
            with self._wait_for_page_refresh():
                click_element_using_mouse_event(self.locator.signin_btn)
            self.se2lib.wait_until_page_does_not_contain_element(self.locator.process_popup, timeout=120)
        else:
            click_element_using_mouse_event(self.locator.signin_btn)