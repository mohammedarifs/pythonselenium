from selenium import webdriver


def test_demorun():
    driver=webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    print(driver.title)
    driver.close()