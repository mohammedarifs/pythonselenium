from selenium import webdriver


def test_demorun():
    driver=webdriver.Chrome()
    driver.get("https://www.udemy.com/")
    print(driver.title)
    driver.close()