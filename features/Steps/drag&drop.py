from behave import given,when, then
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
PATH = "C:\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
@given(u'user is in url page https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):

    driver.get('https://qavbox.github.io/demo/dragndrop/')

@given(u'two boxes appeared')
def step_impl(context):
    drag = driver.find_element_by_id('draggable')
    drop = driver.find_element_by_id('droppable')
    action = ActionChains(driver)
    action.drag_and_drop(drag, drop).perform()

@when(u'user select "Drag" Box')
def step_impl(context):
    print('action done')

@when(u'Drop it to "Drop here" box')
def step_impl(context):
    print("drang and drop done")

@then(u'Dropped text appears')
def step_impl(context):
    msg = driver.find_element_by_id('dropText').text
    print(msg)
    driver.close()
