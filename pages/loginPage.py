# create class
class LoginPage ():
    # create constructors
    def __init__(self, driver):
        self.driver = driver
        # create locators/objects
        self.networkmonitor_link_xpath = "//a[@id='monitor_menu']/span"
        self.networkname_link_linkText = "PD00MIAW001"
        self.username_textbox_id = "usr"
        self.password_textbox_id = "pwd"
        self.login_button_xpath = "(//button[@type='submit'])[2]"

    # create functions/action methods

    def click_networkmonitor(self):
        self.driver.find_element_by_xpath ( self.networkmonitor_link_xpath ).click ()

    def click_networkname(self):
        self.driver.find_element_by_link_text ( self.networkname_link_linkText ).click ()

    def enter_username(self, username):
        self.driver.find_element_by_id ( self.username_textbox_id ).click ()
        self.driver.find_element_by_id ( self.username_textbox_id ).clear ()
        self.driver.find_element_by_id ( self.username_textbox_id ).send_keys ( username )

    def enter_password(self, password):
        self.driver.find_element_by_id ( self.password_textbox_id ).click ()
        self.driver.find_element_by_id ( self.password_textbox_id ).clear ()
        self.driver.find_element_by_id ( self.password_textbox_id ).send_keys ( password )

    def click_login(self):
        self.driver.find_element_by_xpath ( self.login_button_xpath ).click ()
