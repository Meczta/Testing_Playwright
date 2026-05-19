from playwright.sync_api import Page

class OutlookSignInPage:
    def __init__ (self, page:Page):
        self.page = page
        self.field_email = page.locator("type=email")
        self.button_use_password = page.locator("text=Use your password")
        self.field_password = page.locator("name=passwd")
        self.addEmail_buttonCancel = page.locator("text=Cancel")

    def fill_sign_in(self, email):
        self.field_email.fill(email)
    
    def click_use_password(self):
        self.button_use_password.click()

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_cancel(self):
        self.addEmail_buttonCancel.click()

    def sign_in(self, email, password):
        self.fill_sign_in(email)
        self.click_use_password()
        self.fill_password(password)