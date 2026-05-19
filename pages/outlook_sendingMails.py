from playwright.sync_api import Page

class OutlookSendingMailsPage:
    def __init__ (self, page:Page):
        self.page = page
        self.button_new_message = page.locator("text=New mail")
        self.field_to = page.locator("#0")
        self.field_cc = page.locator("#1")
        self.field_subject = page.locator('placeholder="Add a subject"')
        self.button_send = page.locator('title="Send (Ctrl+Enter)"')

    def click_new_message(self):
        self.button_new_message.click()

    def fill_to(self, email):
        self.field_to.fill(email)
    def fill_cc(self, email):
        self.field_cc.fill(email)

    def fill_subject(self, subject):
        self.field_subject.fill(subject)

    def click_send(self):
        self.button_send.click()

    def send_mail(self, to_email, cc_email, subject):
        self.click_new_message()
        self.fill_to(to_email)
        self.fill_cc(cc_email)
        self.fill_subject(subject)
        self.click_send()

