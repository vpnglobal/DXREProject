import time
from selenium import webdriver

driver = webdriver.Chrome (executable_path="C:/Users/Vinay/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe" )
driver.implicitly_wait (10)
driver.maximize_window()
driver.get ( "http://localhost:8989/" )

driver.find_element_by_xpath ( "//a[@id='monitor_menu']/span" ).click ()
driver.find_element_by_link_text ( "PD00MIAW001" ).click ()
driver.find_element_by_id ( "usr" ).click ()
driver.find_element_by_id ( "usr" ).clear ()
time.sleep(5)
driver.find_element_by_id ( "usr" ).send_keys ("admin")
driver.find_element_by_id ( "pwd" ).click ()
driver.find_element_by_id ( "pwd" ).clear ()
driver.find_element_by_id ( "pwd" ).send_keys ( "password" )
driver.find_element_by_xpath ( "(//button[@type='submit'])[2]" ).click ()
driver.find_element_by_xpath ( "//a[@id='monitor_menu']/span" ).click ()
time.sleep(5)
driver.find_element_by_xpath (
    "//div[@class='bootstrap-switch bootstrap-switch-wrapper bootstrap-switch-on bootstrap-switch-mini bootstrap-switch-animate']//i[@class='fa fa-link']" ).click ()
time.sleep(5)
driver.find_element_by_xpath ( "(//button[@type='button'])[3]" ).click ()
driver.close ()
driver.quit()
print("Test completed")


