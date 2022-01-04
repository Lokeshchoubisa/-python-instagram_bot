from selenium import webdriver
from bs4 import BeautifulSoup
import time,requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def insta_bot_send_text(x,y):
    n=int(input('enter number of time to end text'))
    driver=webdriver.Firefox(executable_path='C:\\Users\\lokes\\PycharmProjects\\lok\\geckodriver.exe')
    driver.get('https://instagram.com')
    time.sleep(3)
    elem=driver.find_element_by_xpath('//input[@name="username"]')
    elem.send_keys('your username') 
    elem1=driver.find_element_by_name('password')
    elem1.send_keys('your password')
    elem1.submit()
    #click on inbox
    time.sleep(5)
    turn_off_save=driver.find_element_by_xpath('//button[text()="Not Now"]')
    turn_off_save.click()
    time.sleep(1)
    turn_off_noti=driver.find_element_by_xpath('//button[text()="Not Now"]')
    turn_off_noti.click()
    time.sleep(1)
    inbox=driver.find_element_by_xpath('//a[@class="xWeGp"]')
    inbox.click()
    time.sleep(3)
    send_text=driver.find_element_by_xpath('//button[text()="Send Message"]')
    send_text.click()
    time.sleep(2)
    enter_text=driver.find_element_by_name('queryBox')
    enter_text.send_keys(f'{x[0]}')
    time.sleep(1)
    click_on_entered_text=driver.find_element_by_xpath('//button[@class="dCJp8 "]')
    click_on_entered_text.click()
    click_on_next=driver.find_element_by_css_selector('div.rIacr')
    click_on_next.click()
    time.sleep(2)
    for i in range(n):
        send_text=driver.find_element_by_xpath('//textarea[@placeholder="Message..."]')
        send_text.send_keys(f"{y}")
        send_text.send_keys(Keys.ENTER)





def insta_story():
    driver=webdriver.Firefox(executable_path='C:\\Users\\lokes\\PycharmProjects\\lok\\geckodriver.exe')
    driver.get('https://instagram.com')
    time.sleep(3)
    elem=driver.find_element_by_xpath('//input[@name="username"]')
    elem.send_keys('username')
    elem1=driver.find_element_by_name('password')
    elem1.send_keys('password')
    elem1.submit()
    #click on inbox
    time.sleep(5)
    turn_off_save=driver.find_element_by_xpath('//button[text()="Not Now"]')
    turn_off_save.click()
    time.sleep(1)
    turn_off_noti=driver.find_element_by_xpath('//button[text()="Not Now"]')
    turn_off_noti.click()
    time.sleep(1)
    watch_story=driver.find_element_by_xpath("//div[contains(@class,'eebAO')]")
    watch_story.click()
    time.sleep(2)
    while True:
        try:
            skip_story: WebElement=driver.find_element_by_xpath('//button[@class="ow3u_"]')
            skip_story.click()
        except:
            print('searching...')



def input_press():
    try:
        num = int(input())
        print(num)
    except:
        print('enter the interger number')
        num=input_press()
    return num

print('''welcome to insta bot
press 1 to send message a number of time
press 2 to watch all story 

''')
numm=input_press()
if numm==1:
    message = input("enter text to send")
    n = input('enter username')
    username = []
    username.append(n)
    insta_bot_send_text(username,message)
if numm==2:
    insta_story()

