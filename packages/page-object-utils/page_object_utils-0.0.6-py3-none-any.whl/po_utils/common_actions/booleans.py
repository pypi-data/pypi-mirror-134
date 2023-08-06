"""
    by_locator        : tuple --> (<selenium By object>, <selector string>)
    attribute         : str   --> 'attribute of an html element'
    text              : str   --> 'text of the element'
    is_case_sensitive : bool  --> boolean to toggle case sensitivity
"""

from po_utils.common_actions.waits import wait_for_page_to_load, wait_until_displayed


@wait_until_displayed
@wait_for_page_to_load
def has_attribute(self, by_locator: tuple, attribute: str) -> bool:
    return self._driver.find_element(*by_locator).get_attribute(attribute) != None


@wait_until_displayed
@wait_for_page_to_load
def has_text(self, by_locator: tuple, text: str, is_case_sensitive:bool=False) -> bool:
    element_text = self._driver.find_element(*by_locator).text

    if is_case_sensitive:
        return element_text == text
    return element_text.lower() == text.lower()


@wait_for_page_to_load
def is_visible(self, by_locator: tuple) -> bool:
    try:
        el = self._driver.find_element(*by_locator)
        return el.is_displayed()
    except Exception:
        return False
