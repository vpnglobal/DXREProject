import time
from utils import utils as utils
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.logoutPage import LogoutPage
import moment
import allure

@pytest.mark.usefixtures("test_setup")
class Test_webLogin ():

    def test_login(self):
        driver =self.driver
        driver.get (utils.URL )
        login = LoginPage(driver)
        login.click_networkmonitor ()
        login.click_networkname ()
        time.sleep ( 5 )
        login.enter_username ( utils.USERNAME )
        login.enter_password ( utils.PASSWORD )
        login.click_login ()
    def test_logout(self):
        try:
            driver = self.driver
            logout = LogoutPage(driver)
            logout.click_networkmonitorlogout ()
            time.sleep ( 5 )
            logout.click_logoutlink ()
            time.sleep ( 5 )
            logout.click_logout ()
            x = driver.title
            assert x == "Network onitor"
        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now ().strftime ( "%d-%m-%Y_%H-%M-%S" )
            testName = utils.whoami ()
            screenshotName = testName + "_" + currTime
            allure.attach ( self.driver.get_screenshot_as_png (), name=screenshotName,
                            attachment_type=allure.attachment_type.PNG )
            driver.get_screenshot_as_file (
                "C:/Users/Vinay/PycharmProjects/DXRE/screenshot/" + screenshotName + ".png" )
            raise
        except:
            print("There was an exception")
            currTime = moment.now ().strftime ( "%d-%m-%Y_%H-%M-%S" )
            testName = utils.whoami ()
            screenshotName = testName + "_" + currTime
            allure.attach ( self.driver.get_screenshot_as_png (), name=screenshotName,
                            attachment_type=allure.attachment_type.PNG )
            driver.get_screenshot_as_file (
                "C:/Users/Vinay/PycharmProjects/AutomationFramework_1/screenshot/" + screenshotName + ".png" )
            raise
        else:
            print("No exception occured")
        finally:
            print("Test Completed successfully ")

