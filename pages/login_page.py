from playwright.sync_api import Page

class LoginPage:
    def __init__ (self, page:Page):
        self.page = page
        self.accept_terms_checkbox = page.locator("[type='checkbox']")
        self.mail_name_input = page.locator("#id-field-login")
        self.password_input = page.locator("#id-field-password")
        self.password_repeat_input = page.locator("#id-field-password-repeat")
        self.first_name_input = page.locator("#id-field-first-name")
        self.last_name_input = page.locator("#id-field-last-name")
        self.day_of_birth_input = page.locator("[placeholder='Число']")
        self.month_of_birth_select = page.get_by_role("textbox", name="Місяць")
        self.year_of_birth_input = page.locator("[placeholder='Рік']")
        self.sender_name_input = page.locator("#id-field-sender-name")
        self.recpvery_email_input = page.locator("#id-field-recovery-email")
        self.mobile_number_input = page.locator("#id-field-mobile")
        self.get_code_button = page.locator("text=Отримати код")
        self.create_account_button = page.locator("text=Зареєструвати скриньку")

    def accept_terms(self):
        self.accept_terms_checkbox.click()

    def enter_mail_name(self, mail_name):
        self.mail_name_input.fill(mail_name)
    
    def enter_password(self, password):
        self.password_input.fill(password)

    def enter_password_repeat(self, password_repeat):
        self.password_repeat_input.fill(password_repeat)

    def enter_first_name(self, first_name):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name_input.fill(last_name)

    def enter_day_of_birth(self, day):
        self.day_of_birth_input.fill(day)

    def select_month_of_birth(self, month):
        self.month_of_birth_select.click()
        #self.month_of_birth_select.select_option(text=month)
        self.page.get_by_role("button", name=month).click()


    def enter_year_of_birth(self, year):
        self.year_of_birth_input.fill(year)

    def enter_sender_name(self, sender_name):
        self.sender_name_input.fill(sender_name)

    def enter_recovery_email(self, recovery_email):
        self.recpvery_email_input.fill(recovery_email)

    def enter_mobile_number(self, mobile_number):
        self.mobile_number_input.fill(mobile_number)

    def click_get_code(self):
        self.get_code_button.click()

    def click_create_account(self):
        self.create_account_button.click()

    def fill_registration_form(self, mail_name, password, first_name, last_name, day, month, year, sender_name, recovery_email, mobile_number):
        self.enter_mail_name(mail_name)
        self.enter_password(password)
        self.enter_password_repeat(password)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_day_of_birth(day)
        self.select_month_of_birth(month)
        self.enter_year_of_birth(year)
        self.enter_sender_name(sender_name)
        self.enter_recovery_email(recovery_email)
        self.enter_mobile_number(mobile_number)