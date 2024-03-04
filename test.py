from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#initialize web driver
service = Service(executable_path="C:/Users/HP/.wdm/drivers/chromedriver/win32/114.0.5735.90/chromedriver.exe")

#create the testing method
def do_test(email,pass1,pass2,what_to_display):
    #open the target webpage
    driver.get('http://127.0.0.1:5500/testscript/test.html')
    # find the signup button, email, password 1 and password2 input fields by id
    bn=driver.find_element(by=By.ID,value="btnSign")
    mail_field=driver.find_element(by=By.ID,value="email")
    pass1_field=driver.find_element(by=By.ID,value="pass")
    pass2_field=driver.find_element(by=By.ID,value="pass2")

    # send inputs to the input fields as the email,pass1,pass2 to the respective filds
    mail_field.send_keys(email)
    pass1_field.send_keys(pass1)
    pass2_field.send_keys(pass2)
    # click the Sign up button
    bn.click()

    #intialize initialize the div to be displayed, whether fail div or success div as provided in the parameter
    results=driver.find_element(by=By.ID,value=what_to_display)
    
    try:
        # if the div dispalyed, if disaplyed output test successfull
        assert results.is_displayed() and not print("Test was successfull") 
    except:
        #if assertion error,then Test failed
        print("Test has failed")


with webdriver.Chrome(service=service) as driver:
    #correct details epecting success div 
    do_test("password@gmail.com","Pass100","Pass100","success")
    #incorrect email expecting fail div
    do_test("nicasiomugendi","MUgendi11","Mugendi11","fail")
    #unmatching passwords ecpecting fail div
    do_test("password@gmail.com","Pass100","Pass200","fail")
    #short password expecting fail div
    do_test("password@gmail.com","Pass1","Pass1","fail")
    #password without a number expecting fail div
    do_test("password@gmail.com","Password","Password","fail")
    
    do_test("passwordmail.com","Pa","Password","fail")

"""
all the tests were successful implying that the logic for
verifying the registration details was well implemented
"""

