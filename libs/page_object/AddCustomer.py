from PageObjectLibrary import PageObject
import re
from common import *

class AddCustomer(PageObject):
    IS_DYNAMIC = True
    PAGE_URL = "/react-admin-demo/#/customers"

    _locators = {
        "create_btn": '//.MuiToolbar-regular.css-fwjex > div > a//',
        "first_name": '//#first_name//',
        "last_name": '//#last_name//',
        "email": '//#email//',
        "birthday": '//#birthday//',
        "address": '//#address//',
        "city": '//#city//',
        "state": '//#stateAbbr//',
        "zipcode": '//#zipcode//',
        "password": '//#password//',
        "confirm_pwd": '//#confirm_password//',
        "save_btn": '//.css-fhj390 > div > button//',


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

    def wait_for_save_button_appears(self, timeout=2):
        """
            Wait for save button appears!
        """
        self.se2lib.wait_until_element_is_visible(self.locator.save_btn, timeout)

    def wait_for_create_button_appears(self, timeout=2):
        """
            Wait for create button appears!
        """
        self.se2lib.wait_until_element_is_visible(self.locator.create_btn, timeout)

    def click_save_button(self, wait_refresh='true'):
        """Click the save button"""
        if wait_refresh == 'true':
            with self._wait_for_page_refresh():
                click_element_using_mouse_event(self.locator.save_btn)
            self.se2lib.wait_until_page_does_not_contain_element(self.locator.process_popup, timeout=120)
        else:
            click_element_using_mouse_event(self.locator.save_btn)

    def click_create_button(self, wait_refresh='true'):
        """Click the create button"""
        if wait_refresh == 'true':
            with self._wait_for_page_refresh():
                click_element_using_mouse_event(self.locator.create_btn)
            self.se2lib.wait_until_page_does_not_contain_element(self.locator.process_popup, timeout=120)
        else:
            click_element_using_mouse_event(self.locator.create_btn)

    def enter_first_name(self, first_name):
        """Type the given text into the first name field """
        input_text_with_retry(self.locator.first_name, first_name)

    def enter_last_name(self, last_name):
        """Type the given text into the last name field """
        input_text_with_retry(self.locator.last_name, last_name)

    def enter_email(self, email):
        """Type the given text into the email field """
        input_text_with_retry(self.locator.email, email)

    def enter_birthday(self, birthday):
        """Type the given text into the birthday field """
        input_text_with_retry(self.locator.birthday, birthday)

    def enter_address(self, address):
        """Type the given text into the address field """
        input_text_with_retry(self.locator.address, address)

    def enter_city(self, city):
        """Type the given text into the city field """
        input_text_with_retry(self.locator.city, city)

    def enter_state(self, state):
        """Type the given text into the state field """
        input_text_with_retry(self.locator.state, state)

    def enter_zipcode(self, zipcode):
        """Type the given text into the zipcode field """
        input_text_with_retry(self.locator.zipcode, zipcode)

    def enter_confirm_pwd(self, confirm_pwd):
        """Type the given text into the password field """
        input_text_with_retry(self.locator.confirm_pwd, confirm_pwd)

    def enter_new_customer_password(self, password):
        """Type the given text into the password field """
        input_text_with_retry(self.locator.password, password)



