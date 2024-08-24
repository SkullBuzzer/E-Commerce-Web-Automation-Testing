'''
################################################################################################################
Objective: Test case is to check the new user registeration for application and validate the respective messages
Author: M Gurubasava
Date: 29-04-2024
################################################################################################################
'''
import time
import pytest
from Utility_Classes.Baseclass import BaseClass
from Page_Objects.LoginPage import LoginPage, validate_conf_message_and_page_title_after_user_reg
from Utility_Classes.customLogger import LogGen

EXP_REG_CONF_MSG = "Thank you for registering with Main Website Store."
EXP_PAGE_TITLE = "My Account"

class TestUserRegistration(BaseClass):
    """ Test case class for user registeration which has all test cases related to new user creation """

    logger = LogGen.get_logs()

    @pytest.mark.smoke
    def test_user_registration(self, get_user_details):
        self.logger.info(" *********** TestUserRegistration ******************* ")
        self.logger.info("*********** test case started *******************")
        lp = LoginPage(self.driver)
        lp.click_on_new_reg_link()
        lp.enter_first_name(get_user_details['first_name'])
        lp.enter_last_name(get_user_details['last_name'])
        lp.enter_user_email_id(get_user_details['email'])
        lp.enter_password(get_user_details['password'])
        lp.re_enter_password(get_user_details['conf_password'])
        lp.click_on_register_btn()
        self.logger.info("*********** user created successfully *******************")
    
    @pytest.mark.smoke
    def test_validate_user_registration(self):   
        validate_conf_message_and_page_title_after_user_reg(self.driver, EXP_REG_CONF_MSG, EXP_PAGE_TITLE)
    
    def test_logout_from_application(self):
        lp = LoginPage(self.driver)
        lp.click_profile_toggle()
        lp.click_on_signout()
        self.logger.info("*********** logged out from application *******************")
