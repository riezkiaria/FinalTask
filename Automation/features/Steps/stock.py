from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
 
driver= webdriver.Chrome()

driver.get("https://app.jubelio.com/login")

username_input = driver.find_element('name','email')
password_input = driver.find_element('name','password')
username_input.send_keys("qa.rakamin.jubelio@gmail.com")
password_input.send_keys("Jubelio123!")
login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/button')
login_button.click()

@given('I am on the home page')
def step_impl(context):
    driver.get("https://app.jubelio.com/home/getting-started")

@when('I click on the goods page')
def step_impl(context):
    goods = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/nav/div/div/ul/li[2]/a/span[1]')
    goods.click()
    stock = driver.find_element(By.XPATH,'//*[@id="wrapper"]/nav/div/div/ul/li[2]/ul/li[2]/a/span')
    stock.click()
    time.sleep(1)

@when('I click the stock goods button')
def step_impl(context):
    stock_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]/span[1]')
    stock_button.click()

@when('I enter the name of product')
def step_impl(context):
    stock_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]/span[1]')
    stock_button.click()
    time.sleep(2)
    product_name = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/span/div/span')
    ActionChains(driver).double_click(product_name).perform()
    input_name = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/div[1]/input')
    input_name.send_keys("Huawei")
    time.sleep(2)
    input_name.send_keys(Keys.ENTER)
    time.sleep(2)

@when('I enter the number of product')
def step_impl(context):
    stock_name = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/span/div/div')
    ActionChains(driver).double_click(stock_name).perform()
    input_stock = driver.find_element(By.XPATH,'/html/body/div[6]/div/input')
    input_stock.send_keys("10")
    time.sleep(2)
    input_stock.send_keys(Keys.ENTER)
    time.sleep(4)

@when('I click on save button')
def step_impl(context):
    save_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[3]/div/button')
    save_button.click()
    time.sleep(5)
@then('a notfication pops up that the data is saved')
def step_impl(context):
    assert  driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]')