from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\softwares\\chromedriver_win\\chromedriver.exe")
driver.get("http://www.facebook.com")
driver.find_element_by_id("email").send_keys("user_name")
driver.find_element_by_id("pass").send_keys("password")
driver.find_element_by_id("u_0_b").click()

