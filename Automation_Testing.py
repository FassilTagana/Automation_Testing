# Created by: Fassil Tagana.
# Created on: 02/01/2023
# The program is used to run automated test in web environment.
# ____________________________________________________________________________________________________
import time
import HTMLTestRunner
import unittest
from selenium import webdriver
# from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import Page_Elements
import datetime


class Testing_Project(unittest.TestCase):
    def setUp(self):
        try:
            txt = "                                            Automation Testing Project:\n"
            title = txt.title()
            print(title)
            current_time = datetime.datetime.now()
            print(f'Testing time: {current_time}\n')
            s = Service("C:\\Drivers\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=s)
            self.driver.maximize_window()
            self.driver.get(Page_Elements.Page_URl)

            if WebDriverWait(self.driver, 10).until(EC.title_contains("nopCommerce")):
                print("1. Web loading was successfully!")
                time.sleep(3)
            else:
                print("1. Error - step Failed!")
        except:
            print("1. Error! -Web loading Failed!!")
            self.fail("1.Error - The Element was not found!")

    def test_A_sign_up(self):

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.register_button_by_xpath))).click()
            # # time.sleep(2)
            # self.driver.execute_script("window.scrollTo(0, Y)")
            print("2. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("2. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("5. Error - The Element was not found! and clicked")
        try:
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, Y)")
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.register_button_by_xpath))).click()
            time.sleep(1)
            print("3. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("3. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("3. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.male_gender_button_by_xpath))).click()
            print("4. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("4. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("4. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.first_name_by_xpath))).send_keys(Page_Elements.first_name)
            time.sleep(2)
            print("5. The element was found and was inserted")
        except:
            print("5. Error! -The element was not found!")
            self.fail("5. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.last_name_by_xpath))).send_keys(Page_Elements.last_name)
            time.sleep(1)
            print("6. The element was found and was inserted")
        except:
            print("6. Error! -The element was not found!")
            self.fail("6. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.day_one_button_by_xpath))).click()
            time.sleep(1)
            print("7. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("7. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("7. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.month_april_by_xpath))).click()
            time.sleep(2)
            print("8. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("8. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("8. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.year_1998_by_xpath))).click()
            print("9. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("9. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("9. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.email_by_xpath))).send_keys(Page_Elements.email)
            time.sleep(2)
            print("10. The element was found and was inserted")
        except:
            print("10. Error! -The element was not found!")
            self.fail("10. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.company_name_by_xpath))).send_keys(Page_Elements.company_name)
            time.sleep(1)
            print("11. The element was found and was inserted")
        except:
            print("11. Error! -The element was not found!")
            self.fail("11. Error - The Element was not found!")

        try:
            self.driver.execute_script("window.scrollTo(0, Y)")
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.password_by_xpath))).send_keys(Page_Elements.password)
            time.sleep(1)
            print("12. The element was found and was inserted")
        except:
            print("12. Error! -The element was not found!")
            self.fail("12. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.confirm_password_by_xpath))).send_keys(Page_Elements.password)
            time.sleep(2)
            print("13. The element was found and was inserted")
        except:
            print("13. Error! -The element was not found!")
            self.fail("13. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.register_second_button_by_xpath))).click()
            time.sleep(2)
            print("14. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            # self.driver.get_screenshot_as_file("Screenshots/Login_Failed.png")
            print("14. Error! -The element was not found and clicked!")
            self.fail("14. Error - The Element was not found! and clicked")

        try:
            if 'Your registration completed' in self.driver.page_source:
                self.driver.get_screenshot_as_file("Screenshots/Sign_Up_Succeed.png")
                time.sleep(2)
                print('15. Sign up process succeed :) ')
            else:
                self.driver.get_screenshot_as_file("Screenshots/Sign_up_Failed.png")
                self.fail("15. Sign up process succeed :) ")
        except:
            self.driver.get_screenshot_as_file("Screenshots/Sign_up_Failed.png")
            print("15. Sign up process Failed :) ")
            self.fail("15. Sign up process Failed :)")

    def test_B_log_in_and_purchase_items(self):

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.login_button_by_xpath))).click()
            time.sleep(2)
            print("2. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("2. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("5. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.email_by_xpath))).send_keys(Page_Elements.email)
            time.sleep(2)
            print("3. The element was found and was inserted")
        except:
            print("3. Error! -The element was not found!")
            self.fail("2. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.password_by_xpath))).send_keys(Page_Elements.password)
            time.sleep(2)
            print("4. The element was found and was inserted")
        except:
            print("4. Error! -The element was not found!")
            self.fail("2. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.log_in_second_button_by_xpath))).click()
            time.sleep(2)
            print("5. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("5. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("5. Error - The Element was not found! and clicked")

        try:
            if 'Log out' in self.driver.page_source:
                self.driver.get_screenshot_as_file("Screenshots/Login_Succeed.png")
                time.sleep(1)
                print('6. Login process succeed ')
            else:
                self.driver.get_screenshot_as_file("Screenshots/Login_Failed.png")
                self.fail("6. Login process Failed ")
        except:
            self.driver.get_screenshot_as_file("Screenshots/Login_Failed.png")
            print("6. Login process Failed ")
            self.fail("6. Login process Failed")
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.computers_tab_button_by_xpath))).click()
            time.sleep(2)
            print("7. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("7. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("7. Error - The Element was not found! and clicked")

        try:
            self.driver.execute_script("window.scrollTo(0, 400)")
            # self.driver.execute_script("window.scrollTo(0, Y)")
            # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.desktops_button_by_xpath))).click()
            time.sleep(2)
            print("8. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("8. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("5. Error - The Element was not found! and clicked")

        try:
            self.driver.execute_script("window.scrollTo(0, 420)")
            time.sleep(3)
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.add_to_cart1_button_by_xpath))).click()
            time.sleep(5)
            print("9. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("9. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("9. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.add_to_cart2_button_by_xpath))).click()
            time.sleep(5)
            print("10. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Test1_sign_up_succeed.png")
        except:
            print("10. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("filename.png")
            self.fail("10. Error - The Element was not found! and clicked")

        try:
            self.driver.execute_script("window.scrollTo(100, 0)")
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.shopping_cart_button_by_xpath))).click()
            time.sleep(5)
            print("11. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("11. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("11. Error - The Element was not found! and clicked")

        try:
            self.driver.execute_script("window.scrollTo(0, 600)")
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID, Page_Elements.checkbox_term_by_id))).click()
            time.sleep(2)
            print("12. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("12. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("12. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.checkout_button_by_xpath))).click()
            time.sleep(2)
            print("13. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("13. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("13. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.israel_country_by_xpath))).click()
            time.sleep(2)
            print("14. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("14. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("14. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.city_by_xpath))).send_keys(Page_Elements.city)
            time.sleep(2)
            print("15. The element was found and was inserted")
        except:
            print("15. Error! -The element was not found!")
            self.fail("2. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.address1_by_xpath))).send_keys(Page_Elements.address1)
            time.sleep(2)
            print("16. The element was found and was inserted")
        except:
            print("16. Error! -The element was not found!")
            self.fail("2. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.zip_code_by_xpath))).send_keys(Page_Elements.zip_code)
            time.sleep(2)
            print("17. The element was found and was inserted")
        except:
            print("17. Error! -The element was not found!")
            self.fail("2. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.phone_number_by_xpath))).send_keys(Page_Elements.phone_number)
            time.sleep(2)
            print("18. The element was found and was inserted")
        except:
            print("18. Error! -The element was not found!")
            self.fail("2. Error - The Element was not found!")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.continue_button1_by_xpath))).click()
            time.sleep(3)
            print("19. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("19. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("19. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.continue_button2_by_xpath))).click()
            time.sleep(3)
            print("20. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("20. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("20. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.continue_button3_by_xpath))).click()
            time.sleep(3)
            print("21. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("21. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("21. Error - The Element was not found! and clicked")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.continue_button4_by_xpath))).click()
            time.sleep(3)
            print("22. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("22. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("22. Error - The Element was not found! and clicked")

        try:
            self.driver.execute_script("window.scrollTo(0, 1500)")
            # self.driver.execute_script("window.scrollTo(0, Y)")
            # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, Page_Elements.confirm_button_by_xpath))).click()
            time.sleep(3)
            print("23. The element was found and was clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/Test1_sign_up_succeed.png")
        except:
            print("23. Error! -The element was not found and clicked!")
            # self.driver.get_screenshot_as_file("Screenshots/filename.png")
            self.fail("23. Error - The Element was not found! and clicked")

        try:
            if 'Your order has been successfully processed!' in self.driver.page_source:
                self.driver.get_screenshot_as_file("Screenshots/Item_Purchase_Succeed.png")
                time.sleep(1)
                print('24. Login process succeed ')
            else:
                self.driver.get_screenshot_as_file("Screenshots/Item_purchase_Failed.png")
                self.fail("24. Login process Failed ")
        except:
            self.driver.get_screenshot_as_file("Screenshots/Item_purchase_Failed.png")
            print("24. Item purchase  process Failed ")
            self.fail("24. Item purchase  Failed")

    def tearDown(self):
        print("*** Test was over ***")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='Reports'))  # Creating a report
