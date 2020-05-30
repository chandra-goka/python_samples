from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\softwares\\chromedriver_win\\chromedriver.exe")
driver.get("http://www.google.com")
element = driver.find_element_by_name("q");
element.send_keys("top 10 python books");
element.submit();

results = driver.find_elements_by_xpath("//div[@class='g']//div[@class='r']//a[not(@class)]");
print(len(results))
for result in results:
    print(result.get_attribute("href"))
