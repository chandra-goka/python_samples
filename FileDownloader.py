from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

LOGIN_URL = "https://squaw.nic.fr//login"
USER = "CSC_SQUAW"
PASS = "v2SsAgzqtTHwu6Jg"
DOWNLOAD_URL = "https://squaw.nic.fr/app.php/download/domain-names-{}.{}"
download_dir = "D:\\softwares\\filedownloads\\"
driver_path = "D:\\softwares\\chromedriver_win\\chromedriver.exe"

def enable_download(browser):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    return chrome_options;

if __name__ == '__main__':
    day = datetime.today().strftime('%Y%m%d')
    DOWNLOAD_URL = DOWNLOAD_URL.format(day,"zip")
    driver = webdriver.Chrome(executable_path=driver_path,options=setting_chrome_options())
    driver.get(LOGIN_URL)
    driver.find_element_by_id("login_username").send_keys(USER)
    driver.find_element_by_id("login_password").send_keys(PASS)
    driver.find_element_by_class_name("authentication_btn").click()
    enable_download(driver)
    time.sleep(10)
    driver.get(DOWNLOAD_URL)