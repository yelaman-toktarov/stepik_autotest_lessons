from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)
WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
driver.find_element(By.ID,"book").click()
y = driver.find_element(By.ID, "input_value")
x = int(y.text)
n = str(math.log(abs(12 * math.sin(x))))
answer = driver.find_element(By.ID, "answer")
n = (n)
answer.send_keys(n)
driver.find_element(By.ID,"solve").click()
alert = driver.switch_to.alert
n = alert.text
driver.quit()
print(n)
