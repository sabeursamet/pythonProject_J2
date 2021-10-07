from selenium import webdriver

class WebDriver:
    def init(self, driver):
        self.driver = driver

    def enter(self):
        return self.driver

    def exit(self, exc_type, exc_val, exc_tb):
        self.driver.quit()