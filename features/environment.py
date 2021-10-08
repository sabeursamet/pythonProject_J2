import os
from selenium import webdriver

from pages.drag_drop import drag_drop

PATH = "\drivers\chromedriver.exe"


def before_scenario(context, scenario):
    dir = os.getcwd()
    print(dir)
    context.browser = webdriver.Chrome(executable_path = dir + PATH)
    context.browser.maximize_window()
    context.dd = drag_drop(context.browser)


def after_scenario(context, scenario):
    context.browser.close()
