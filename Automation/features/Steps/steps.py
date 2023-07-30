from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
 
driver= webdriver.Chrome()

@given('I am on the login page')
def step_impl(context):
    driver.delete_all_cookies
    driver.get("https://app.jubelio.com/login")

@when('I enter valid login credentials')
def step_impl(context):
    username_input = driver.find_element('name','email')
    password_input = driver.find_element('name','password')
    username_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input.send_keys("Jubelio123!")
    time.sleep(1)

@when('I click the login button')
def step_impl(context):
    login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()
    time.sleep(3)
@then('I should be redirected to homepage')
def step_impl(context):
    assert  "home" in driver.current_url
    
    

driver= webdriver.Chrome()

@given('I am on the jubelio login page')
def step_impl(context):
    driver.delete_all_cookies
    driver.get("https://app.jubelio.com/login")

@when('I enter my email and leave the password field empty')
def step_impl(context):
    username_input = driver.find_element('name','email')
    password_input = driver.find_element('name','password')
    username_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input.send_keys(" ")
    time.sleep(2)

@when('I click the masuk button')
def step_impl(context):
    login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()
@then('an error should appear telling me that password must be filled')
def step_impl(context):
    assert  driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/div[2]/div/span') 