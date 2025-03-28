import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture()
def set_driver():
    yield webdriver.Chrome()

def test_demorun(set_driver):

    driver=set_driver
    driver.get("https://www.udemy.com/")
    print(driver.title)
    driver.close()


def test_demosearchtxt(set_driver):
    driver=set_driver
    driver.get("https://www.udemy.com/")
    driver.find_element(By.XPATH,'//input[@data-testid="search-input"]').send_keys("Python selenium"+(Keys.RETURN))
    driver.close()

def test_checklogin(set_driver):
    driver=set_driver
    driver.get("https://www.udemy.com/")
    driver.find_element(By.XPATH,'//span[text()="Log in"]').click()
    driver.close()