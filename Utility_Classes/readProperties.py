""" This file can be used read the data from different files like ini and .yaml and .py files """

import yaml
import configparser
import random
import openpyxl

config = configparser.RawConfigParser()
config.read(filenames=".\\Test_Suite_Configuration\\config.ini")

with open(".\\Test_Data\\user_info.yaml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

with open(file=".\\Test_Data\\shipping_info.yaml", mode="r") as file:
    data_shipping = yaml.load(file, Loader=yaml.FullLoader)

excel_file = openpyxl.load_workbook(".\\Test_Data\\invalid_cred.xlsx")

class ReadConfig:
    """ Class to read data from the config file """
 
    @staticmethod
    def get_application_url():
        """ method to get the app url from config file """
        url = config.get("NopCommerce_Login_Info", "base_url")
        return url
    
    @staticmethod
    def get_username():
        """ method to get the username from config file """
        username = config.get("NopCommerce_Login_Info", "username")
        return username
    
    @staticmethod
    def get_password():
        """ method to get the password from config file """
        password = config.get("NopCommerce_Login_Info", "password")
        return password

    @staticmethod
    def get_user_info():
        """ method to read all data from yaml file """
        user_info = []
        for user_data in [
            "first_name", "last_name", "email", "password",
            "conf_password"]:
            if user_data == "first_name":
                fname = data["NEW_USER_INFO"][user_data] + str(random.randint(1, 999))
                user_info.append(fname)
            elif user_data == "last_name":
                lname = data["NEW_USER_INFO"][user_data] + str(random.randint(1, 999))
                user_info.append(lname)
            elif user_data == "email":
                email = "guru"+str(random.randint(1, 999))+data["NEW_USER_INFO"][user_data]
                user_info.append(email)
            else:
                user_info.append(data["NEW_USER_INFO"][user_data])
        return user_info
    
    @staticmethod
    def get_exist_user_info():
        """ method to read all data from yaml file """
        user_info = []
        for user_data in [
            "first_name", "last_name", "email", "password",
            "conf_password"]:
            user_info.append(data["EXIST_USER_INFO"][user_data])
        return user_info

    @staticmethod
    def read_login_cred_from_excel():
        """ method to read data from excel """
        workbook = excel_file
        sheet_to_read = workbook["Invalid_Cred"]
        all_values = [list(row) for row in sheet_to_read.iter_rows(values_only = True)]
        login_data = []
        user_cred = {}
        for val in all_values[1:]:
            user_cred = {'username':val[0], 'password':val[1]}
            login_data.append(user_cred)
        return login_data

    @staticmethod
    def get_product_info():
        " method to get the product info "
        product_name = data["PRODUCT_INFO"]["product_name"]
        return product_name

    @staticmethod
    def get_shipping_info():
        " method to get shipping info from yaml file "
        shipping_info = {}
        for info in ["city", "addr", "pin_code", "ph_no"]:
            shipping_info[info] = data_shipping["SHIPPING_INFO"][info]
        return shipping_info
