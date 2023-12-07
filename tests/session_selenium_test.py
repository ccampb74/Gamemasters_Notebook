'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pre-condition: user "c" with password "c" exists 
class SigninTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get('http://localhost:5000/')

    #check to see if a registered user can access the campaign creation page
    def test_successful_campaign(self):
        signin_button = self.browser.find_element(By.XPATH,'//button[@class="modern-button"][.="Sign In"]')
        signin_button.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('c')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('c')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        new_campaign = self.browser.find_element(By.LINK_TEXT,"Create New Campaign")
        new_campaign.click()
        page = self.browser.current_url
        self.assertEqual('http://localhost:5000/new_campaign', page)
    
    #check to see if an unregistered user can access the campaign creation page
    def test_unsuccessful_campaign(self):
        new_campaign = self.browser.find_element(By.LINK_TEXT,"Create New Campaign")
        new_campaign.click()
        message = self.browser.find_element(By.TAG_NAME, "h5")
        self.assertTrue(message.text.startswith("Please log in before creating a campaign"))

if __name__ == '__main__':
    unittest.main()