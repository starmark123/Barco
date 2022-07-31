from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/starmark/Downloads/pytest_toturial/chromedriver")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys('Admin')
driver.find_element_by_id("txtPassword").send_keys('admin123')
driver.find_element_by_id("btnLogin").click()

driver.implicitly_wait(3)
print("Click")

print("Test complete")