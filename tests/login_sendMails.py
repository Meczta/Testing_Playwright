from playwright.sync_api import Page
from pages.oulook_main import OutlookMainPage
from pages.outlook_signin import OutlookSignInPage
from pages.outlook_sendingMails import OutlookSendingMailsPage
from config.credentials import USER_LOGIN, USER_PASSWORD, SEND_TO, CC_TO
import pytest

def test_book_room_valid_data(page, context):
    page.goto("https://outlook.live.com")
    user_page = OutlookMainPage(page)

    user_page.click_sign_in()
    login_page = OutlookSignInPage(page)
    login_page.sign_in(USER_LOGIN, USER_PASSWORD)
    sending_mail_page = OutlookSendingMailsPage(page)
    text = ['text1', 'text2']
    for i in text:
        sending_mail_page.send_mail(SEND_TO, CC_TO, i)