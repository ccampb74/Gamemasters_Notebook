'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pre-condition: a campaign with id="55" already exists and user "c" with password "c" exists 
class SigninTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        # self.browser = webdriver.Edge()
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:5000/')

    #check to see if an unregistered user can create a campaign 
    def test_unsucessful_campaign(self):
        signin_button = self.browser.find_element(By.XPATH,'//button[text()="Sign In"]')
        signin_button.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('c')
        password = self.browser.find_element(By.ID, 'password')
        self.assertIsNotNone(passwd)
        password.send_keys('c')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        page = self.browser.current_url
        # new_campaign = self.browser.find_elements(By.TAG_NAME, 'button') [0]
        # new_campaign.click()
        self.assertEqual('http://localhost:5000/users', page)


if __name__ == '__main__':
    unittest.main()