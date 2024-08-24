""" This module contains all locators, action methods and validation methods related shipping cart page """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ShippingCartPage:
    """ class having locators and action methods related to shipping cart page """
     
    edi_link_xpath = "//a[contains(text(),'Edit')]"
    updated_prod_info_xpath = "//td[@class='product']/div[1]"
    terms_cond_checkbox_xpath = "//input[@id='termsofservice']"
    checkout_btn_xpath = "//button[@id='checkout']"
    country_dropdown_xpth = "//select[@id='BillingNewAddress_CountryId']"
    city_textbox_xpath = "//input[@id='BillingNewAddress_City']"
    addr_textbox_xpath = "//input[@id='BillingNewAddress_Address1']"
    pincode_textbox_xpath = "//input[@id='BillingNewAddress_ZipPostalCode']"
    phno_textbox_xpath = "//input[@id='BillingNewAddress_PhoneNumber']"
    cont_btn_xpath = "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[1]/div[2]/div[1]/button[2]"
    shipping_method_radio_xpath = "//input[@id='shippingoption_1']"
    cont_btn_checkout = "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[3]/div[2]/form[1]/div[2]/button[1]"
    cont_after_pament = "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[4]/div[2]/div[1]/button[1]"
    cont_btn_after_shipping_addr = "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[5]/div[2]/div[1]/button[1]"
    confirm_btn_xpath = "//button[contains(text(),'Confirm')]"
    confirm_msg = "//strong[contains(text(),'Your order has been successfully processed!')]"
     
    def __init__(self, driver):
        self.driver1 = webdriver.Chrome()
        self.driver1 = driver
    
    def click_on_edit_link(self):
        edit_link = self.driver1.find_element(By.XPATH, self.edi_link_xpath)
        edit_link.click()
    
    def get_updated_product_info(self):
        info = self.driver1.find_element(By.XPATH, self.updated_prod_info_xpath)
        return info.text

    def click_terms_and_conditions_checkbox(self):
        checkbox = self.driver1.find_element(By.XPATH, self.terms_cond_checkbox_xpath)
        checkbox.click()
        checkbox.is_selected()

    def click_on_checkout_btn(self):
        chkout_btn = self.driver1.find_element(By.XPATH, self.checkout_btn_xpath)
        chkout_btn.click()
    
    def get_page_title(self):
        page = self.driver1.title
        return page
    
    def select_country(self, text):
        drop_down = self.driver1.find_element(By.XPATH, self.country_dropdown_xpth)
        sel = Select(drop_down)
        sel.select_by_visible_text(text)

    def enter_shipping_info(self, city, addr, pin_code, ph_no):
        self.driver1.find_element(By.XPATH, self.city_textbox_xpath).send_keys(city)
        self.driver1.find_element(By.XPATH, self.addr_textbox_xpath).send_keys(addr)
        self.driver1.find_element(By.XPATH, self.pincode_textbox_xpath).send_keys(pin_code)
        self.driver1.find_element(By.XPATH, self.phno_textbox_xpath).send_keys(ph_no)
        self.driver1.find_element(By.XPATH, self.cont_btn_xpath).click()

    def click_on_cont_btn(self):
        btn = self.driver1.find_element(By.XPATH, self.cont_btn_xpath)
        btn.click()

    def select_shipping_method(self):
        radio_btn = self.driver1.find_element(By.XPATH, self.shipping_method_radio_xpath)
        radio_btn.click()
        radio_btn.is_enabled()
    
    def click_continue_to_checkout(self):
        cont_btn = self.driver1.find_element(By.XPATH, self.cont_btn_checkout)
        cont_btn.click()
    
    def click_continue_after_payment(self):
        cont_btn = self.driver1.find_element(By.XPATH, self.cont_after_pament)
        cont_btn.click()

    def click_continue_after_shipping_addr_verfy(self):
        cont_btn = self.driver1.find_element(By.XPATH, self.cont_btn_after_shipping_addr)
        cont_btn.click()

    def click_on_confirm_btn(self):
        conf_btn = self.driver1.find_element(By.XPATH, self.confirm_btn_xpath)
        conf_btn.click()
    
    def get_conf_message(self):
        conf_msg = self.driver1.find_element(By.XPATH, self.confirm_msg)
        return conf_msg.text

#################################################################################
# Python keywords to validate the expected results in Shipping Cart web page
#################################################################################

def validate_updated_prod_info_in_shipping_cart_page(driver, exp_prod_info=None):
    cart_page = ShippingCartPage(driver)
    act_prod = cart_page.get_updated_product_info()
    assert exp_prod_info in act_prod, f"Expected product info not found. Expected '{exp_prod_info} but found '{act_prod}"

def validate_page_title(driver, exp_title):
    cart_page = ShippingCartPage(driver)
    act_title = cart_page.get_page_title()
    assert act_title == exp_title, f"Expected page not found. Expected '{exp_title} but found '{act_title}"

def validate_conf_message_after_placing_order(driver, exp_msg):
    cart_apge = ShippingCartPage(driver)
    act_msg = cart_apge.get_conf_message()
    try:
        assert act_msg == exp_msg, f"Expected message not found. Expected '{exp_msg} but found '{act_msg}"
    except AssertionError:
        driver.save_screenshot(".\\Screenshots_and_Output\\checkout_prod_error.png")
