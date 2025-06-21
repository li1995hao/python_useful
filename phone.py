import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from time import sleep
import random
import string
# 设置 Chrome 驱动
service = Service(ChromeDriverManager().install())
# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.javascript": 1  # 1 = Allow JavaScript
})
# chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode if needed

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
# 设置一些firefox选项，比如无头模式
firefox_options.headless = True


for _ in range(1000000000000):
    driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://zodiculture.com/")
    sleep(5)
    driver.refresh()
    sleep(6)
    phone_input = driver.find_element(By.ID, "phonenumber")
    phone_input.send_keys(Keys.CONTROL + "a")
    phone_input.send_keys(Keys.BACKSPACE)


    phone_like_str = "070" + ''.join(random.choices(string.digits, k=8))
    phone_input.send_keys(phone_like_str)
    next_button = driver.find_element(By.ID, "buttonid")  # 用id定位
    sleep(2)
    next_button.click()
    sleep(2)
    next_button = driver.find_element(By.ID, "submit")  # 用id定位
    next_button.click()
    sleep(1)
    random_letters = ''.join(random.choices(string.ascii_letters, k=10))
    card_input = driver.find_element(By.ID, "cardname")
    card_input.send_keys(random_letters)
    sleep(1)
    arr = np.random.randint(0, 10, 13)  # 生成8个0-9的整数
    random_digits_1 = ''.join(map(str, arr))  # 转成字符串连接起来
    n_input = driver.find_element(By.ID, "cardnumber")
    n_input.send_keys(random_digits_1)
    sleep(1)
    D_input = driver.find_element(By.ID, "cardexpire")
    D_input.send_keys("08")
    sleep(1)
    D_input.send_keys("29")
    sleep(1)
    c_letters = ''.join(random.choices(string.digits, k=3))
    c_input = driver.find_element(By.ID, "cvv")
    c_input.send_keys(c_letters)
    sleep(1)


    next_button = driver.find_element(By.ID, "buttonid")  # 用id定位
    sleep(1)
    next_button.click()
    sleep(5)
    driver.quit()


arr = ["adcccc"]
result = ''
for element in arr:
    result =  result + str(element)