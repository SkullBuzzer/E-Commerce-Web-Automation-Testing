""" This module contains all locators, action methods and validation methods related home page or store page """

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class StorePage:
    """ class having locators and action methods related to NopCommerce store page """

    nopCommercce_link_xpath = "//div[@class='header-logo']/a"
    search_box_xpath = "//input[@id='small-searchterms']"
    search_btn_xpath = "//button[contains(text(),'Search')]"
    product_list_xpath = "//div[@class='product-grid']/div/div/div/div[2]/h2"
    appreal_cat_xpath = "//div[@class='header-menu']/ul[1]/li[3]"
    cloth_prod_xpath = "//div[@class='item-grid']/div[2]/div/h2/a"
    all_prods_xpath = "//div[@class='item-grid']/div/div/div[2]/h2/a"
    sort_dropdown_xpath = "//select[@id='products-orderby']"
    prods_price_xpath = "//div[@class='item-grid']/div/div/div[2]/div[3]/div[1]/span"
    htc_prod_xpath = "//span[contains(text(),'HTC One M8 Android L 5.0 Lollipop')]"
    add_to_wishlist_id = "add-to-wishlist-button-18"
    conf_message_xpath = "//div[@id='bar-notification']//ancestor::p"
    close_icon_xpth = "//span[@class='close']"
    wishlist_link_xpath = "//span[contains(text(),'Wishlist')]"
    wishlist_prod_xpath = "(//div[@class='table-wrapper']//ancestor::a)[2]"
    rem_prod_xpth = "//div[@class='table-wrapper']//ancestor::td/button"
    conf_rem_msg_xpath = "//div[contains(text(),'The wishlist is empty!')]"
    appreal_main_tab_xpath = "(//div[@class='header-menu']//ancestor::a)[9]"
    shoe_option_xpath = "(//ul[@class='sublist first-level']//ancestor::a)[7]"
    shoe_product_xpath = "//body/div[6]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]/a[1]"
    size_dropdown_xpath = "//div[@class='attributes']/dl/dd[1]/select"
    add_to_cart_button_xpath = "//button[@id='add-to-cart-button-25']"
    add_to_cart_cnf_msg_xpath = "//p[@class='content']/a"
    cart_close_icon_xpath = "//body/div[@id='bar-notification']/div[1]/span[1]"
    shipping_cart_xpath = "//span[contains(text(),'Shopping cart')]"
    go_to_cart_btn_xpath = "//button[contains(text(),'Go to cart')]"
    prod_in_cart_xpath = "//a[@class='product-name']"
    

    def __init__(self, driver):
        self.driver1 = webdriver.Chrome()
        self.driver1 = driver
    
    def click_on_nopComm_icon(self):
        nop_icon = self.driver1.find_element(By.XPATH, self.nopCommercce_link_xpath)
        nop_icon.click()
    
    def input_product_name_to_search(self, prod_name):
        search_box = self.driver1.find_element(By.XPATH, self.search_box_xpath)
        search_box.send_keys(prod_name)
    
    def click_on_search_btn(self):
        search_btn = self.driver1.find_element(By.XPATH, self.search_btn_xpath)
        search_btn.click()
    
    def get_product_list(self):
        prod_list = self.driver1.find_elements(By.XPATH, self.product_list_xpath)
        return prod_list
    
    def click_on_Apparel_main_tab(self):
        main_tab = self.driver1.find_element(By.XPATH, self.appreal_cat_xpath)
        main_tab.click()
        return main_tab

    def click_on_cloths_tab(self):
        cloth_tab = self.driver1.find_element(By.XPATH, self.cloth_prod_xpath)
        cloth_tab.click()
    
    def sort_prods(self, value):
        sort_drop_down = self.driver1.find_element(By.XPATH, self.sort_dropdown_xpath)
        select = Select(sort_drop_down)
        select.select_by_value(value)
    
    def get_all_sorted_products(self):
        prods = self.driver1.find_elements(By.XPATH, self.all_prods_xpath)
        return prods

    def get_all_prods_price(self):
        prods_price = self.driver1.find_elements(By.XPATH, self.prods_price_xpath)
        return prods_price

    def wait_for_product_to_display(self):
        wait = WebDriverWait(self.driver1, timeout=10)
        product_ele = self.driver1.find_element(By.XPATH, self.htc_prod_xpath)
        wait.until(expected_conditions.visibility_of(product_ele))
        product_ele.click()

    def click_on_add_to_wishlist_button(self):
        wish_list_btn = self.driver1.find_element(By.ID, self.add_to_wishlist_id)
        wish_list_btn.click()
    
    def get_confirm_message(self):
        msg = self.driver1.find_element(By.XPATH, self.conf_message_xpath)
        return msg

    def click_on_close_icon(self):
        close_icon = self.driver1.find_element(By.XPATH, self.close_icon_xpth)
        close_icon.click()

    def click_on_wishlist_icon(self):
        link = self.driver1.find_element(By.XPATH, self.wishlist_link_xpath)
        link.click()
    
    def get_wishlist_page_title(self):
        page = self.driver1.title
        return page
    
    def get_wishlist_product(self):
        prod = self.driver1.find_element(By.XPATH, self.wishlist_prod_xpath)
        return prod
    
    def click_on_remove_icon(self):
        remove_btn = self.driver1.find_element(By.XPATH, self.rem_prod_xpth)
        remove_btn.click()
    
    def get_conf_msg_on_prod_rem(self):
        conf_msg = self.driver1.find_element(By.XPATH, self.conf_rem_msg_xpath)
        return conf_msg
    
    def select_shoes_option(self):
        action = ActionChains(self.driver1)
        main_tab = self.driver1.find_element(By.XPATH, self.appreal_main_tab_xpath)
        sub_option = self.driver1.find_element(By.XPATH, self.shoe_option_xpath)
        action.move_to_element(main_tab).move_to_element(sub_option).click().perform()

    def select_required_product(self):
        shoe_prod = self.driver1.find_element(By.XPATH, self.shoe_product_xpath)
        shoe_prod.click()
    
    def select_product_size(self, size):
        drop_down = self.driver1.find_element(By.XPATH, self.size_dropdown_xpath)
        sel = Select(drop_down)
        sel.select_by_index(size)

    def click_on_add_to_cart_btn(self):
        btn = self.driver1.find_element(By.XPATH, self.add_to_cart_button_xpath)
        btn.click()

    def get_conf_msg_on_adding_prod_cart(self):
        msg = self.driver1.find_element(By.XPATH, self.add_to_cart_cnf_msg_xpath)
        return msg.text
    
    def click_on_close_icon(self):
        icon = self.driver1.find_element(By.XPATH, self.cart_close_icon_xpath)
        icon.click()
    
    def navigate_to_cart_page(self):
        action = ActionChains(self.driver1)
        shipping_cart = self.driver1.find_element(By.XPATH, self.shipping_cart_xpath)
        go_to_cart = self.driver1.find_element(By.XPATH, self.go_to_cart_btn_xpath)
        action.move_to_element(shipping_cart).move_to_element(go_to_cart).click().perform()
    
    def get_product_from_cart_page(self):
        prod = self.driver1.find_element(By.XPATH, self.prod_in_cart_xpath)
        return prod.text
    
#################################################################################
# Python keywords to validate the expected results in Storage web page
#################################################################################

def validate_display_of_products_based_on_search_criteria(driver, exp_products):
    storage_page = StorePage(driver)
    act_prods = storage_page.get_product_list()
    assert len(act_prods) == len(exp_products)
    try:
        for i in range (len(exp_products)):
            assert exp_products[i] == act_prods[i].text, f"Expected Products not found. Expected '{exp_products[i]}' but found '{act_prods[i].text}"
    except AssertionError as msg:
        driver.save_screenshot(".\\Screenshots_and_Output\\error_prod.png")
        raise AssertionError(str(msg))

def check_products_dislayed_based_on_name_sorting(driver, exp_cloth_prods, asc):
    storage_page = StorePage(driver)
    act_cloth_prods = storage_page.get_all_sorted_products()
    assert len(act_cloth_prods) == len(exp_cloth_prods)
    if asc == True:
        for i in range(len(act_cloth_prods)):
            assert act_cloth_prods[i].text == exp_cloth_prods[i], f"Expected Products not found. Expected '{exp_cloth_prods[i]}' but found '{act_cloth_prods[i].text}"
    else:
        for i in range(len(act_cloth_prods)):
            assert act_cloth_prods[i].text == exp_cloth_prods[i], f"Expected Products not found. Expected '{exp_cloth_prods[i]}' but found '{act_cloth_prods[i].text}"

def check_products_displayed_based_on_price_sorting(driver, exp_prods_price, asc=None):
    storage_page = StorePage(driver)
    act_prices = storage_page.get_all_prods_price()
    assert len(act_prices) == len(exp_prods_price)
    if asc:
        for i in range(len(act_prices)):
            assert act_prices[i].text == exp_prods_price[i], f"Expected Products not found. Expected '{exp_prods_price[i]}' but found '{act_prices[i].text}"
    else:
        for i in range(len(act_prices)):
            assert act_prices[i].text == exp_prods_price[i], f"Expected Products not found. Expected '{exp_prods_price[i]}' but found '{act_prices[i].text}"

def validate_confirm_message_after_adding_to_wishlist(driver, exp_msg):
    storage_page = StorePage(driver)
    act_msg = storage_page.get_confirm_message()
    assert act_msg.text == exp_msg, f"Expected conf message not found. Expected '{exp_msg}' but found '{act_msg}'"

def validate_product_in_wishlist_page(driver, exp_page, exp_product):
    storage_page = StorePage(driver)
    act_title = storage_page.get_wishlist_page_title()
    act_product = storage_page.get_wishlist_product()
    try:
        assert act_title == exp_page, f"Expected conf message not found. Expected '{exp_page}' but found '{act_title}'"
    except AssertionError:
        driver.save_screenshot(".\\Screenshots_and_Output\\wishlist_error1.png")
    try:
        assert act_product.text == exp_product, f"Expected product not found. Expected '{exp_product}' but found '{act_product.text}'"
    except AssertionError:
        driver.save_screenshot(".\\Screenshots_and_Output\\wishlist_error2.png")

def validate_conf_message_on_rem_product(driver, exp_msg):
    storage_page = StorePage(driver)
    conf_msg = storage_page.get_conf_msg_on_prod_rem()
    assert conf_msg.text == exp_msg, f"Expected product not found. Expected '{exp_msg}' but found '{conf_msg.text}'"

def validate_conf_message_on_adding_prod_to_cart(driver, exp_msg):
    storage_page = StorePage(driver)
    act_msg = storage_page.get_conf_msg_on_adding_prod_cart()
    assert act_msg == exp_msg, f"Expected message not found. Expected '{exp_msg} but found '{act_msg}"
    print(act_msg)

def validate_prod_in_cart_page(driver, exp_product):
    storage_page = StorePage(driver)
    act_prod = storage_page.get_product_from_cart_page()
    assert act_prod == exp_product, f"Expected product not found. Expected '{exp_product}' but found '{act_prod.text}'"