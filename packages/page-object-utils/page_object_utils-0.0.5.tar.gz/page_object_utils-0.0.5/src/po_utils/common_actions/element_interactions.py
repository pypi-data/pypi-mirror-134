"""
    by_locator        : tuple --> (<selenium By object>, <selector string>)
    x_offset          : int   --> integer value of x offset in pixels
    y_offset          : int   --> integer value of y offset in pixels
    x_destination     : int   -->  integer value of x location on page
    y_desitination    : int   --> integer value of y location on page
    by_locator_source : tuple --> (<selenium By object>, <selector string>)
    by_locator_target : tuple --> (<selenium By object>, <selector string>)
    clear_first       : bool  --> toggle for clearing input field before writing text to it
    press_enter       : bool  --> toggle for sending the ENTER key to an input field after writing to it
"""

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from po_utils.common_actions.waits import wait_for_page_to_load, wait_until_displayed, wait_until_not_displayed


@wait_until_displayed
@wait_for_page_to_load
def click_element(self, by_locator:tuple, x_offset:int=0, y_offset:int=0) -> None:
    # I hate clicking
    element = WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator))
    scroll_height = self._driver.execute_script('return document.body.scrollHeight')
    window_size = self._driver.get_window_size()['height']
    if element.location['y'] > (scroll_height - .5 * window_size):
        self._driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    elif element.location['y'] < (.5 * window_size):
        self._driver.execute_script('window.scrollTo(0, 0)')
    else:
        self._driver.execute_script(f"window.scrollTo({element.location['x']}, {element.location['y'] - .5 * window_size});")
    if x_offset == 0 and y_offset == 0:
        try:
            WebDriverWait(self._driver, self._driver_wait_time).until(EC.element_to_be_clickable(by_locator)).click()
        except:
            WebDriverWait(self._driver, self._driver_wait_time).until(EC.element_to_be_clickable(by_locator)).click()
    else:
        ActionChains(self._driver).move_to_element_with_offset(WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator)), x_offset, y_offset).click().perform()


@wait_until_displayed
@wait_for_page_to_load
def click_and_drag_element_by_offset(self, by_locator:tuple, x_destination:int, y_desitination:int) -> None:
    element = WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator))
    ActionChains(self._driver).drag_and_drop_by_offset(element, x_destination, y_desitination).perform()


@wait_until_displayed
@wait_for_page_to_load
def click_and_drag_element(self, by_locator_source:tuple, by_locator_target:tuple) -> None:
    source = WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator_source))
    target = WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator_target))
    ActionChains(self._driver).drag_and_drop(source, target).perform()


@wait_until_displayed
@wait_for_page_to_load
def send_text_to_element(self, by_locator:tuple, text:str, clear_first:bool=True, press_enter:bool=False) -> None:
    if clear_first:
        self._driver.find_element(*by_locator).clear()
    self._driver.find_element(*by_locator).send_keys(text)
    if press_enter:
        self._driver.find_element(*by_locator).send_keys(Keys.ENTER)


@wait_until_displayed
@wait_for_page_to_load
def hover_over_element(self, by_locator:tuple) -> None:
    element = self._driver.find_element(*by_locator)
    ActionChains(self._driver).move_to_element(element).perform()
