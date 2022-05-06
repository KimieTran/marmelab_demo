from PageObjectLibrary import PageObject
import re
from common import *


class CustomerInfo(PageObject):
    IS_DYNAMIC = True
    PAGE_URL = "/react-admin-demo/#/customers/%s"

    _locators = {
        "customer_info_first_name": '//#first_name//',
        "customer_info_last_name": '//#last_name//',
        "customer_info_email": '//#email//',
        "customer_info_birthday": '//#birthday',
        "customer_info_city": '//#city//',
        "customer_info_state": '//#stateAbbr//',
        "customer_info_zipcode": '//#zipcode//',
        "customer_info_address": '//#address//',
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
        template = re.compile(r'%s' % '.*' + regexmatch + '.*$')
        if template.match(location) is None:
            message = "Expected location to end with " + \
                      templateStr + " but it did not"
            raise Exception(message)
        return True

    def wait_for_customer_info_first_name_contains_text(self,text, timeout=2):
        """
            Wait for customer info first name contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_first_name, text, timeout)

    def wait_for_customer_info_last_name_contains_text(self,text, timeout=2):
        """
            Wait for customer info first name contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_last_name, text, timeout)

    def wait_for_customer_info_email_contains_text(self,text, timeout=2):
        """
            Wait for customer info email contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_email, text, timeout)

    def wait_for_customer_info_birthday_contains_text(self,text, timeout=2):
        """
            Wait for customer info birthday contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_birthday, text, timeout)

    def wait_for_customer_info_city_contains_text(self, text, timeout=2):
        """
            Wait for customer info city contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_city, text, timeout)

    def wait_for_customer_info_state_contains_text(self, text, timeout=2):
        """
            Wait for customer info state contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_state, text, timeout)

    def wait_for_customer_info_zipcode_contains_text(self, text, timeout=2):
        """
            Wait for customer info zipcode contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_zipcode, text, timeout)

    def wait_for_customer_info_address_contains_text(self, text, timeout=2):
        """
            Wait for customer info address contains text!
        """
        self.se2lib.wait_until_element_contains(self.locator.customer_info_address, text, timeout)


