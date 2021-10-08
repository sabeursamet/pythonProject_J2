import os
from selenium import webdriver
from os import getcwd



def before_scenario(context,scenario):

    dir = os.getcwd()
    print(dir)
    context.browser=webdriver.Chrome(executable_path=dir + "\drivers\chromedriver.exe")
    context.browser.maximize_window()

def after_scenarion(context,scenario):
    context.browser.close()