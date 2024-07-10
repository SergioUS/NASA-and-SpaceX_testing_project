#Helper for VBratuhin_Rideshare_Unitest

from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By


def delay():
    time.sleep(random.randint(1, 3))


Spacex_url = "https://www.spacex.com/"
Rideshare_url = "https://rideshare.spacex.com/search"


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, 500)")
    delay()
    driver.execute_script("window.scrollTo(0, 1050)")
    delay()
    driver.execute_script("window.scrollTo(0, 1500)")
    delay()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    delay()
    driver.execute_script("window.scrollTo(0, 0)")


#Completing the previous sections.
def previous_step1(driver):
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
    delay()
    driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
    delay()
def previous_step2(driver):
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
    delay()
    driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
    delay()
    driver.find_element(By.XPATH, "(//a[contains(@class,'arrow-button button wipe')])[2]").click()
    delay()
def previous_step3(driver):
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
    delay()
    driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
    delay()
    driver.find_element(By.XPATH, "(//a[contains(@class,'arrow-button button wipe')])[2]").click()
    delay()
    driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[4]").click()
    delay()
def previous_step4(driver):
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
    delay()
    driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
    delay()
    driver.find_element(By.XPATH, "(//a[contains(@class,'arrow-button button wipe')])[2]").click()
    delay()
    driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[4]").click()
    delay()
    driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
    delay()

def previous_step5(driver):
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
    delay()
    driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
    delay()
    driver.find_element(By.XPATH, "(//a[contains(@class,'arrow-button button wipe')])[2]").click()
    delay()
    driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[4]").click()
    delay()
    driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
    delay()
    driver.find_element(By.XPATH, "//div[contains(text(),'Contact Information')]")
    driver.execute_script("window.scrollTo(0, 500)")

def previous_step6(driver):
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
    delay()
    driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
    delay()
    driver.find_element(By.XPATH, "(//a[contains(@class,'arrow-button button wipe')])[2]").click()
    delay()
    driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[4]").click()
    delay()
    driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
    delay()
    driver.find_element(By.XPATH, "//div[contains(text(),'Contact Information')]")
    driver.execute_script("window.scrollTo(0, 800)")
