from playwright.sync_api import Page

class MainPage:
    def __init__ (self, page:Page):
        self.page = page
        self.sign_in_button = page.locator("iframe[name=\"mail widget\"]").content_frame.get_by_role("link", name="Створити скриньку")

    def click_sign_in(self):
        self.sign_in_button.click()