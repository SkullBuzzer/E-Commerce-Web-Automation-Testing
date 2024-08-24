""" This module contains all locators, action methods and validation methods related login page """

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """ class having locators and action methods related to login page """
    
    REG_LINK = "//div[@class='panel header']/ul//following-sibling::li[3]"
    FIRSTNAME_TEXT_FIELD = "//input[@id='firstname']"
    LASTNAME_TEXT_FIELD = "//input[@id='lastname']"
    EMAIL_TEXT_FIELD = "//input[@id='email_address']"
    PASSWORD_TEXT_FIELD = "//input[@id='password']"
    CONF_PWD_TEXT_FIELD = "//input[@id='password-confirmation']"
    SUBMIT_BUTTON = "//button[@title='Create an Account']"
    REG_CONF_MSG = "//div[contains(text(),'Thank you for registering with Main Website Store.')]"
    LOGOUT_TOGGLE = "//div[@class='panel header']/ul/li[2]/span/button"
    SIGN_OUT_LINK = "//li[@class='customer-welcome active']/div/ul/li[3]/a"
    EXST_USER_REG_ERROR_MSG = "//div[@class='page messages']/div[2]/div/div/div"

    def __init__(self, driver, username=None, passsword=None):
        self.driver = driver
        self.username = username
        self.password = passsword

    def click_on_new_reg_link(self):
        """ click on register link to enter user details """
        reg_link = self.driver.find_element(By.XPATH, self.REG_LINK)
        reg_link.click()
    
    def enter_first_name(self, first_name):
        """ enter user first name """
        fname = self.driver.find_element(By.XPATH, self.FIRSTNAME_TEXT_FIELD)
        fname.clear()
        fname.send_keys(first_name)
    
    def enter_last_name(self, last_name):
        """ enter users last name """
        lname = self.driver.find_element(By.XPATH, self.LASTNAME_TEXT_FIELD)
        lname.clear()
        lname.send_keys(last_name)

    def enter_user_email_id(self, email_id):
        """ Enter user email id """
        email = self.driver.find_element(By.XPATH, self.EMAIL_TEXT_FIELD)
        email.clear()
        email.send_keys(email_id)
    
    def enter_password(self, password):
        """ enter password """
        pwd = self.driver.find_element(By.XPATH, self.PASSWORD_TEXT_FIELD)
        pwd.clear()
        pwd.send_keys(password)
    
    def re_enter_password(self, conf_password):
        pwd = self.driver.find_element(By.XPATH, self.CONF_PWD_TEXT_FIELD)
        pwd.clear()
        pwd.send_keys(conf_password)
    
    def click_on_register_btn(self):
        """ click on register link to create new user """
        reg_btn = self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON)
        reg_btn.click()
    
    def get_reg_conf_message(self):
        """ method to get confirmation message after reg """
        conf_msg = self.driver.find_element(By.XPATH, self.REG_CONF_MSG)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.REG_CONF_MSG)))
        return conf_msg.text
    
    def click_profile_toggle(self):
        """ method to click on cont btn after registeration """
        prof_togle = self.driver.find_element(By.XPATH, self.LOGOUT_TOGGLE)
        prof_togle.click()
    
    def click_on_signout(self):
        """ method to get error message for duplicate user registeration """
        sign_out = self.driver.find_element(By.XPATH, self.SIGN_OUT_LINK)
        sign_out.click()

    def get_error_msg_for_exst_user_reg(self):
        """ return error message from web page for invalid login"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.EXST_USER_REG_ERROR_MSG)))
        error_msg = self.driver.find_element(By.XPATH, self.EXST_USER_REG_ERROR_MSG)
        return error_msg.text


#################################################################################
# Python keywords to validate the expected results in login web page
#################################################################################

def validate_conf_message_and_page_title_after_user_reg(driver, exp_msg, exp_titile):
    """ method to validate the message after user registeration """
    lp = LoginPage(driver)
    act_msg = lp.get_reg_conf_message()
    act_pg_title = driver.title
    try:
        assert act_pg_title == exp_titile, f"Expected page not found. Expected '{exp_titile}' but found '{act_pg_title}'"
    except AssertionError as msg:
        driver.save_screenshot(".\\Screenshots_and_Output\\user_reg_page.png")
        raise AssertionError(str(msg) + "Screenshot saved")
    try:
        assert act_msg == exp_msg, f"Expected message not found. Expected '{exp_msg}' but found '{act_msg}'."
    except AssertionError as msg:
        driver.save_screenshot(".\\Screenshots_and_Output\\user_reg_msg.png")
        raise AssertionError(str(msg) + "Screenshot saved")
    

def validate_error_message_for_exist_user_registeration(driver, exp_error_msg):
    """ method used to validate the error message when user try to add duplicate user """
    lp = LoginPage(driver)
    act_error_msg = lp.get_error_msg_for_exst_user_reg()
    try:
        assert act_error_msg == exp_error_msg, f"Expected message not found. Expected '{act_error_msg}' but found '{exp_error_msg}'"
    except AssertionError as msg:
        driver.save_screenshot(".\\Screenshots_and_Output\\exst_user_reg.png")
        raise AssertionError(str(msg) + "Screenshot saved")

def validate_error_msg_for_mandatory_fields(driver, exp_errors:list):
    """ Method used to validate all mandatory fileds for user registeration """
    lp = LoginPage(driver)
    act_errors = lp.get_all_mandatory_fields()
    print(act_errors)
    for error in zip(act_errors, exp_errors):
        try:
            assert error[0] == error[1], f"Expected error message not found. Expected '{error[1]}' but found '{error[0]}"
        except AssertionError:
            driver.save_screenshot(".\\Screenshots_and_Output\\error_mand_fields.png")

def validate_page_title(driver, exp_title):
    """ Method used to validate login page with title """
    act_title = driver.title
    assert act_title == exp_title, f"Expected page not found. Expected '{act_title}' but found '{exp_title}'"

def validate_error_message_for_invalid_credentials(driver, exp_error_msg):
    """ Validates the error message when a user tries to log in with invalid credentials."""
    lp = LoginPage(driver)
    act_error_msg = lp.get_error_msg_for_invalid_login()
    assert act_error_msg == exp_error_msg, f"Expected page not found. Expected '{act_error_msg}' but found '{exp_error_msg}'"
