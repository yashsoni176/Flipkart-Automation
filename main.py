import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

product = input("Enter Product : ")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test Case Started")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(2)
driver.find_element_by_name("q").send_keys(product)
time.sleep(2)
driver.find_element_by_class_name("_34RNph").click()
time.sleep(3)