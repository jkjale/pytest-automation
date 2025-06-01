from difflib import SequenceMatcher
from selenium.common.exceptions import NoSuchElementException

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_element_with_ai(driver, known_locator, all_possible_locators):
    try:
        return driver.find_element(*known_locator)
    except NoSuchElementException:
        print("[AI] Original locator failed. Trying alternatives...")
        for locator in all_possible_locators:
            try:
                elem = driver.find_element(*locator)
                if similar(locator[1], known_locator[1]) > 0.6:
                    print(f"[AI] Found similar element using locator: {locator}")
                    return elem
            except:
                continue
        raise NoSuchElementException("Element not found with any AI-assisted locators.")
