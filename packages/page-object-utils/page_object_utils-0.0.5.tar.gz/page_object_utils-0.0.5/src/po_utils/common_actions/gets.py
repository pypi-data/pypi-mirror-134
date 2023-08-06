"""
    by_locator : tuple --> (<selenium By object>, <selector string>)
    attribute  : str   --> 'attribute of an html element'
"""

from po_utils.common_actions.waits import wait_for_page_to_load, wait_until_displayed, wait_until_not_displayed


@wait_until_displayed
@wait_for_page_to_load
def get_elements(self, by_locator: tuple) -> object:
    return self._driver.find_elements(*by_locator)

@wait_until_displayed
@wait_for_page_to_load
def get_element(self, by_locator: tuple) -> object:
    res = get_elements(self, by_locator)[0]
    return res if res else []

@wait_until_displayed
@wait_for_page_to_load
def get_element_attribute(self, by_locator: tuple, attribute: str) -> object:
    return self._driver.find_element(*by_locator).get_attribute(attribute)

@wait_until_displayed
@wait_for_page_to_load
def get_element_text(self, by_locator: tuple) -> object:
    return self._driver.find_element(*by_locator).text
