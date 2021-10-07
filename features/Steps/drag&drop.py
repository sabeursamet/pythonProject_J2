from behave import given,when, then
from numpy.testing import assert_equal
from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = "C:\drivers\chromedriver.exe"

@given(u'user is in url page https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):
    context.driver = webdriver.Chrome(PATH)
    context.driver.get('https://qavbox.github.io/demo/dragndrop/')

@given(u'two boxes appeared')
def step_impl(context):
    print('page opened')

@when(u'user select "Drag" Box')
def step_impl(context):
    driver = context.driver
    drag = driver.find_element_by_id('draggable')
    drop = driver.find_element_by_id('droppable')
    action = ActionChains(driver)
    action.drag_and_drop(drag, drop).perform()
    print('action done')

@when(u'Drop it to "Drop here" box')
def step_impl(context):
    print("drag and drop done")

@then(u'Dropped text appears')
def step_impl(context):
    driver = context.driver
    msg = driver.find_element_by_id('dropText').text
    assert_equal(msg,'Dropped!')
    driver.close()
