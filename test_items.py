from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Add to basket button is not displayed"

