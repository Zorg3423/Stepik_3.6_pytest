import time


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(10)

    add_to_basket_button = browser.find_element(
        "css selector", "button.btn-add-to-basket"
    )

    assert len(add_to_basket_button) > 0, "Add to basket button is not found"
