from functools import wraps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_page_to_load(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        try:
            WebDriverWait(self.driver, self.__driver_wait_time).until(lambda _: self.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass
        function_call = function(self, *args, **kwargs)
        try:
            WebDriverWait(self.driver, self.__driver_wait_time).until(lambda _: self.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass
        return function_call
    return wrapper


def wait_until_displayed(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        try:
            WebDriverWait(self.driver, self.__driver_wait_time).until(EC.visibility_of_element_located(args[0]))
        except:
            pass
        return function(self, *args, **kwargs)
    return wrapper


def wait_until_not_displayed(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        try:
            WebDriverWait(self.driver, self.__driver_wait_time).until(EC.invisibility_of_element_located(args[0]))
        except:
            pass
        return function(self, *args, **kwargs)
    return wrapper

