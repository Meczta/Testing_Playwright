from pages.login_page import LoginPage
from pages.home_page import MainPage
import pytest
from config.credentials import USER_LOGIN, USER_PASSWORD, FIRST_NAME, LAST_NAME, DAY, MONTH, YEAR, FULL_NAME, EMAIL, PHONE_NUMBER

def test_book_room_valid_data(page, context):
    page.goto("https://www.ukr.net/", wait_until="domcontentloaded")  
    
    main_page = MainPage(page)

    with context.expect_page() as new_page_info:
        main_page.click_sign_in()

        

    new_page = new_page_info.value
    login_page = LoginPage(new_page)

    login_page.accept_terms()
    login_page.fill_registration_form(USER_LOGIN, USER_PASSWORD, FIRST_NAME, LAST_NAME, DAY, MONTH, YEAR, FULL_NAME, EMAIL, PHONE_NUMBER)
    page.pause()