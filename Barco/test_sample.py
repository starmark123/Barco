from selenium import webdriver
import pytest
import time


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/starmark/Downloads/Barco/chromedriver")
        time.sleep(10)
        #driver.maximize_window()

    def test_warranty_valid(self, test_setup):
        driver.get("https://www.barco.com/en/clickshare/support/warranty-info/")
        driver.find_element_by_id("SerialNumber").send_keys('1863552437') # warrenty serial number: 1863552437
        driver.find_element_by_class_name("btn-block").click()
        #m = driver.find_element_by_xpath('//span[normalize-space()]')
        m = driver.find_element_by_xpath("//span[normalize-space()='Minimum 6 characters required']")
        assert not m.is_displayed()
        time.sleep(5)
        driver.close()
        driver.quit()

    def test_warranty_showIsTooShort(self, test_setup):
        driver.get("https://www.barco.com/en/clickshare/support/warranty-info/")
        driver.find_element_by_id("SerialNumber").send_keys('ekjw')
        driver.find_element_by_class_name("btn-block").click()
        m = driver.find_element_by_xpath("//span[normalize-space()='Minimum 6 characters required']")
        assert m.is_displayed()
        time.sleep(5)
        driver.close()
        driver.quit()

    def test_warranty_showIsWrongFormat(self, test_setup):
        driver.get("https://www.barco.com/en/clickshare/support/warranty-info/")
        driver.find_element_by_id("SerialNumber").send_keys('fjaow;awj@')
        driver.find_element_by_class_name("btn-block").click()
        m = driver.find_element_by_xpath("//span[normalize-space()='Please enter a valid serial number']")
        assert m.is_displayed()
        time.sleep(5)
        driver.close()
        driver.quit()

    def test_warranty_showIsRequired(self, test_setup):
        driver.get("https://www.barco.com/en/clickshare/support/warranty-info/")
        driver.find_element_by_id("SerialNumber").send_keys('')
        driver.find_element_by_class_name("btn-block").click()
        m = driver.find_element_by_xpath("//span[normalize-space()='Please specify a serial number']")
        assert m.is_displayed()
        time.sleep(5)
        driver.close()
        driver.quit()

    def test_warranty_50times(self, test_setup):
        driver.get("https://www.barco.com/en/clickshare/support/warranty-info/")
        driver.find_element_by_id("SerialNumber").send_keys('fjaow;awj@')
        for i in range (51):
            driver.find_element_by_xpath("//button[normalize-space()='Get info']").click()
            print ('Click', i, 'times')
        m = driver.find_element_by_xpath("//span[normalize-space()='Please enter a valid serial number']")
        assert m.is_displayed()
        time.sleep(5)
        driver.close()
        driver.quit()
    #
    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test complete")
