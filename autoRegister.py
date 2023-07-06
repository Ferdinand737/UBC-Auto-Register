from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.common.by import By
import time
from twilio.rest import Client

#List of classes you want to register in
#eg. classes = ['COSC 315 101','COSC 360 001','COSC 414 001', 'COSC 360 L02']
classes = ['COSC 499 001', 'COSC 305 L02']

#campus wide login
#eg. cwl = "ljohnson"
#eg. pwd = "verySecurePassword"
cwl = "fhaaben"
pwd = "H%xp'>67FQnZkPU;"

#make an account at twilio.com
#free trial has enough texts
twilio_account = ""
twilio_token = ""

#eg. twilio_phone_number = "+17786981234"
twilio_phone_number = ""

#eg. your_phone_number = "+17786980085"
your_phone_number = ""

browser = webdriver.Chrome()

def login(url):
    try:
        button = browser.find_element(By.XPATH,"(//input[@alt='CWL Login'])[1]")
    except NoSuchElementException:
        #print("Can't find Login button")
        return
    
    button.click()
    try:
        username = browser.find_element(By.XPATH,"//input[@id='username']")
        password = browser.find_element(By.XPATH,"//input[@id='password']")
        login = browser.find_element(By.XPATH,"//input[@value='Login']")
        username.send_keys(cwl)
        password.send_keys(pwd)
        login.click()
    except NoSuchElementException:
        print("Already Logged in")
    
    time.sleep(2)
    browser.get(url)
    time.sleep(2)

def register():
    try:
        browser.find_element(By.XPATH,"//*[text()='Note: this section is full']")
        return False
    except NoSuchElementException:
        register = browser.find_element(By.XPATH,"//a[text()='Register Section']")
        register.click()
        return True

def confirm_and_text(class_):

    #client = Client(twilio_account,twilio_token)

    try:
        browser.find_element(By.XPATH,"//*[contains(text(),'The section was added successfully')]")
      #  client.messages.create(from_ = twilio_phone_number, body = "Successfully Registered in " + class_, to = your_phone_number)
        classes.remove(class_)
        print(f"Successfully registered in {class_}")
    except NoSuchElementException:
      #  client.messages.create(from_ = twilio_phone_number, body = "Failed to register in " + class_, to = your_phone_number)
      print(f"Failed to register in {class_}")

i = 0
while True:
    for class_ in classes:
        
        dept = class_.split(" ")[0]
        course = class_.split(" ")[1]
        section = class_.split(" ")[2]
        url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={}&course={}&section={}".format(dept,course,section)
        browser.get(url)
        time.sleep(2)
        login(url)
        if register():
            confirm_and_text(class_)

    time.sleep(900)
    i += 1
    print("Completed " + str(i) + " iterations")
