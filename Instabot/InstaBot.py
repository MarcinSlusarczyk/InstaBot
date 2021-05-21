import requests
from bs4 import BeautifulSoup
import pymsgbox as pg
from selenium import webdriver 
import time
import pymsgbox
import random
import pymsgbox as pg
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

login = pg.prompt(text='wpisz login')
password = pg.password('wpisz hasło do swojego konta', mask='*')

hashtags = ['polska','warsaw', 'krakow', 'polskadziewczyna', 'polskichlopak', 'poland', 'polishboy', 'girl', 'polishgirl', 'selfie', 'instalove', 'wroclaw', 'wroclove']

# log in

link = f'https://www.instagram.com/'
driver.get(link)
driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

time.sleep(3)

# click functions

time.sleep(random.randint(1,7))

def check_exists_by_xpath(status_xpath):

    try:

        driver.find_element_by_xpath(status_xpath)

    except NoSuchElementException:

        return False

    return True



def check_exists_by_xpath_follow(status_follow):

    try:

        driver.find_element_by_xpath(status_follow)

    except NoSuchElementException:

        return False

    return True


def check_exists_by_xpath_nick(status_nick):

    try:

        driver.find_element_by_xpath(status_nick)

    except NoSuchElementException:

        return False

    return True

for hashtag in random.sample(hashtags, len(hashtags)):
    
    iterration = random.randint(10, 35)
    count = 0

    link = f'https://www.instagram.com/explore/tags/{hashtag}/'
    page = driver.get(link)
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div/div[2]').click()
    time.sleep(6)  
    while True:

        if count > iterration:
                #pause            
                print(f"zmieniam hashtag na - {hashtag}")
                time.sleep(random.randint(100,200))                
                break
            
        # count click pic
        for i in range(1, random.randint(2,6)):
            time.sleep(random.randint(4,10))
            driver.find_element_by_link_text('Dalej').click()
        
        time.sleep(random.randint(1,3))
        
        # check visible elements               

        status_xpath = '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button'
        status_follow = '/html/body/div[6]/div/div/div[4]/button'
        status_nick = '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div/span/a'

        if check_exists_by_xpath(status_xpath) == False:
            time.sleep(random.randint(3,8))
            driver.find_element_by_link_text('Dalej').click()

          
        # set random choice

        for j in range(1, random.randint(1,3)):
            
            if j == 1:
                
                # like
                time.sleep(random.randint(3,5))

                if check_exists_by_xpath(status_xpath) == False:
                    time.sleep(random.randint(3,8))
                    driver.find_element_by_link_text('Dalej').click()
                else:
                    driver.find_element_by_xpath(status_xpath).click()                
                
            
            if j == 2:            
                
                # follow
                count = count + 1 
                print(f"zaobserwowałem - {count}")
                time.sleep(random.randint(3,5))

                if check_exists_by_xpath_nick(status_nick) == False:
                    time.sleep(random.randint(3,5))
                    driver.find_element_by_link_text('Dalej').click()
                else:
                    nick = driver.find_element_by_xpath(status_nick)
                    hover = ActionChains(driver).move_to_element(nick)
                    hover.perform()

                    time.sleep(random.randint(2,3))

                    if check_exists_by_xpath_follow(status_follow) == False:
                        time.sleep(random.randint(3,5))
                        driver.find_element_by_link_text('Dalej').click()
                    else:
                       driver.find_element_by_xpath(status_follow).click()
                                      
                        
            if j == 3:
                
                # like & follow
                count = count + 1
                print(f"zaobserwowałem - {count}")                
                time.sleep(random.randint(3,5))

                if check_exists_by_xpath(status_xpath) == False:
                    time.sleep(random.randint(3,8))
                    driver.find_element_by_link_text('Dalej').click()
                else:
                    driver.find_element_by_xpath(status_xpath).click()

                
                time.sleep(random.randint(3,5))

                if check_exists_by_xpath_nick(status_nick) == False:
                    time.sleep(random.randint(3,5))
                    driver.find_element_by_link_text('Dalej').click()
                else:
                    nick = driver.find_element_by_xpath(status_nick)
                    hover = ActionChains(driver).move_to_element(nick)
                    hover.perform()

                    time.sleep(random.randint(2,3))

                    if check_exists_by_xpath_follow(status_follow) == False:
                        time.sleep(random.randint(3,5))
                        driver.find_element_by_link_text('Dalej').click()
                    else:
                       driver.find_element_by_xpath(status_follow).click() 

                                                                               

