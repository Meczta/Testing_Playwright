from playwright.sync_api import Page

class OutlookMainPage:
    def __init__ (self, page:Page):
        self.page = page
        self.button_sign_in = page.locator("#c-shellmenu_custom_outline_signin_bhvr100_right")

    def click_sign_in(self):
        self.button_sign_in.click()