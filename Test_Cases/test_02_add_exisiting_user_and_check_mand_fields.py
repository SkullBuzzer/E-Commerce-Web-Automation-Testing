'''
#################################################################################################################################
Objective: Test case is to check the mandatory fields in user registeration for application and validate the error messages
Author: M Gurubasava
Date: 29-04-2024
##################################################################################################################################
'''

import pytest
from Utility_Classes.Baseclass import BaseClass
from Page_Objects.LoginPage import LoginPage, validate_error_message_for_exist_user_registeration, validate_error_msg_for_mandatory_fields
from Utility_Classes.readProperties import ReadConfig
from Utility_Classes.customLogger import LogGen

EXP_ERROR_MSG = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."


class TestExistingUserRegistrationAndMandatoryFields(BaseClass):
    """ Test case class with multiple test cases"""

    exs_user_info = ReadConfig.get_exist_user_info()
    logger = LogGen.get_logs()

    @pytest.mark.neagtive
    def test_existing_user_registration(self):
        self.logger.info("****** TestExistingUserRegistrationAndMandatoryFields ******")
        lp = LoginPage(self.driver)
        self.logger.info("****** adding duplicate user ******")
        lp.click_on_new_reg_link()
        lp.enter_first_name(self.exs_user_info[0])
        lp.enter_last_name(self.exs_user_info[1])
        lp.enter_user_email_id(self.exs_user_info[2])
        lp.enter_password(self.exs_user_info[3])
        lp.re_enter_password(self.exs_user_info[4])
        lp.click_on_register_btn()
    
    @pytest.mark.neagtive
    def test_validate_existing_user_error_message(self):
        validate_error_message_for_exist_user_registeration(self.driver, EXP_ERROR_MSG)
