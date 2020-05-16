from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\softwares\\chromedriver_win\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
driver.close()
