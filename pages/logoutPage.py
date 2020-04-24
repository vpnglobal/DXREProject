# create class
import time


class LogoutPage ():
    # create constructors
    def __init__(self, driver):
        self.driver = driver
        # create locators/objects
        self.networkmonitorLogout_link_xpath = "//a[@id='monitor_menu']/span"
        self.logoutlink_xpath = "//div[@class='bootstrap-switch bootstrap-switch-wrapper bootstrap-switch-on bootstrap-switch-mini bootstrap-switch-animate']//i[@class='fa fa-link']"
        self.logout_button_xpath = "(//button[@type='button'])[3]"


    # create functions/action methods

    def click_networkmonitorlogout(self):
        self.driver.find_element_by_xpath ( self.networkmonitorLogout_link_xpath  ).click ()

    def click_logoutlink(self):
        self.driver.find_element_by_xpath(self.logoutlink_xpath).click()
       # self.driver.find_element_by_link_text ( self.logoutlink_xpath ).click ()


    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()