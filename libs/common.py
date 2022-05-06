from robot.libraries.BuiltIn import BuiltIn
import time
import robot.api
import clipboard


class S2l(object):
    @property
    def s2l(self):
        return BuiltIn().get_library_instance('Selenium2Library')


s2lib = S2l()
logger = robot.api.logger


def get_element_to_view(element):
    js_code = """
        function getElementByXpath(path) {
            return document.evaluate(
                path, 
                document, 
                null, 
                XPathResult.FIRST_ORDERED_NODE_TYPE, 
                null).singleNodeValue;
        }

        var elementX = getElementByXpath('""" + element + """');

        var topPos = elementX.offsetTop;

        elementX.scrollIntoViewIfNeeded()
    """
    s2lib.s2l.wait_until_page_contains_element(element, timeout=5)
    s2lib.s2l.execute_javascript(js_code)


def scroll_element_to_bottom(element):
    js_code = """
        function getElementByXpath(path) {
            return document.evaluate(
                path, 
                document, 
                null, 
                XPathResult.FIRST_ORDERED_NODE_TYPE, 
                null).singleNodeValue;
        }
        
        var elementX = getElementByXpath('""" + element + """');
        
        var topPos = elementX.offsetTop;
        
        elementX.scroll(0, elementX.scrollHeight)
    """
    s2lib.s2l.execute_javascript(js_code)


def wait_until_element_is_visible_and_click_element(element, timeout=5):
    s2lib.s2l.scroll_element_into_view(element)
    s2lib.s2l.wait_until_element_is_visible(element, timeout=timeout)
    click_element_using_mouse_event(element)


def select_dropdown_by_value(locator, value):
    s2lib.s2l.wait_until_element_is_visible(locator, timeout=5)
    s2lib.s2l.select_from_list_by_value(locator, str(value))


def click_element_using_mouse_event(element, scroll=1):
    s2lib.s2l.wait_until_element_is_visible(element, timeout=5)
    if scroll:
        s2lib.s2l.scroll_element_into_view(element)
    s2lib.s2l.mouse_down(element)
    time.sleep(0.01)
    s2lib.s2l.mouse_up(element)
    time.sleep(0.01)


def click_element(element, retry=5, scroll=1, timeout=5):
    s2lib.s2l.wait_until_element_is_visible(element, timeout=timeout)
    if scroll:
        try:
            s2lib.s2l.scroll_element_into_view(element)
        except:
            pass
    for re in range(retry):
        try:
            s2lib.s2l.click_element(element)
            return
        except:
            logger.info('Can not click element "{}", retry {} times'.format(element, re+1))
            time.sleep(0.1)


def delete_value_in_field(locator):
    data = s2lib.s2l.get_element_attribute(locator, 'value')
    for del_time in range(0, len(data)):
        s2lib.s2l.press_key(locator, '\\8')


def input_text_with_retry(locator, text):
    text = str(text)
    s2lib.s2l.scroll_element_into_view(locator)
    s2lib.s2l.wait_until_element_is_visible(locator, timeout=5)
    delete_value_in_field(locator)
    inputted = ''
    for retry in range(0, 5):
        s2lib.s2l.input_text(locator, text)
        time.sleep(0.1)
        inputted = str(get_element_attribute_with_retry(locator, 'value'))
        if inputted == text:
            print 'try' + str(retry)
            return
        else:
            delete_value_in_field(locator)
    raise Exception("Can not input '{}' to '{}'. Inputted '{}'".format(text, locator, inputted))


def input_number_to_qc(locator, number, lang='en'):
    if ',' in str(number) or '.' in str(number):
        raise Exception("Input number wrong, number should not contains , or .")
    try:
        number = int(number)
    except:
        input_text_with_retry(locator, number)
        return
    separator = ','
    if lang != 'en':
        separator = '.'
    number = int(number)
    expected_input = number
    expected_input = "{:,}".format(expected_input)
    expected_input = expected_input.replace(',', separator)

    s2lib.s2l.scroll_element_into_view(locator)
    s2lib.s2l.wait_until_element_is_visible(locator, timeout=5)
    delete_value_in_field(locator)
    inputted = ''
    for retry in range(0, 5):
        s2lib.s2l.input_text(locator, number)
        time.sleep(0.1)
        inputted = str(get_element_attribute_with_retry(locator, 'value'))
        if inputted == expected_input:
            print 'try' + str(retry)
            return
        else:
            delete_value_in_field(locator)
    raise Exception("Can not input '{}' to '{}'. Inputted '{}'".format(number, locator, inputted))


def get_element_attribute_with_retry(element, attribute, retry=10):
    for re in range(0, retry):
        try:
            return s2lib.s2l.get_element_attribute(element, attribute)
        except:
            logger.debug("retry {} times to get element {} attribute {}".format(re, element.encode('ascii', 'ignore'),
                                                                                attribute))
    raise Exception('Can not get Element "{}" attribute "{}"'.format(element, attribute))


def generate_list_string_no_duplicate(length, string_len, lower_case=True, upper_case=False, number=False, special_case=False):
    import string
    import random

    list_word = []
    if lower_case:
        choice = string.ascii_lowercase
    if upper_case:
        choice += string.ascii_uppercase
    if number:
        choice += string.digits
    if special_case:
        choice += string.punctuation
    if not lower_case and not upper_case and not number and not special_case:
        choice = string.ascii_letters
    idx = 0
    while len(list_word) < int(length):
        word = ''.join(random.choice(choice) for idx in range(int(string_len)))
        if word not in list_word:
            print 'add: `{}` to list index: `{}`'.format(word, len(list_word))
            list_word.append(word)
        else:
            print 'reject: {}'.format(word)
    return list_word


def set_text_to_clipboard(text):
    clipboard.copy(text)


def clear_clipboard():
    clipboard.copy('')


def delete_text_area(locator):
    s2lib.s2l.press_keys(locator, 'CONTROL+A')
    time.sleep(1)
    s2lib.s2l.press_keys(locator, 'DELETE')
    time.sleep(1)


def paste_text_to_text_area(locator, text):
    delete_text_area(locator)
    for retry in range(10):
        set_text_to_clipboard(text)
        s2lib.s2l.press_keys(locator, 'CONTROL+V')
        try :
            value = get_element_attribute_with_retry(locator, 'value')
            if value == text:
                logger.info('paste: {}\n-------\n real:{}'.format(value, text))
                clear_clipboard()
                return
        except:
            delete_text_area(locator)
            clear_clipboard()
            logger.info('copy paste get something wrong, re-try in {} times'.format(retry))


def generate_list_string_with_subfix(string, length, bracelet_left='', bracelet_right=''):
    list_t = []
    for i in range(1, length+1):
        list_t.append(bracelet_left + string + str(i) + bracelet_right)
    return list_t


def reload_current_page():
    s2lib.s2l.reload_page()


if __name__ == '__main__':

    for a in generate_list_string_no_duplicate(26*26, 2):
        print a
