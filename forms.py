from selenium import webdriver
from os.path import dirname
import time, json

f = open('info.json', "r")
data = json.loads(f.read())
naam = data['naam']
klas = data['klas']
niveau = data['niveau']
week1 = data['week1']
week12 = data['week12']
week2 = data['week2']
week22 = data['week22']
week3 = data['week3']
week32 = data['week32']
dir = (dirname(__file__))


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=dir + '\chromedriver.exe')
driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=l1KfyqeDqEGyyaSoB0fV9Ro_bwbU7-lMqOWu1ARaHFtUNTJPN0xKRVpENkhMQ0hUNVdVSldIM0pNUS4u')
time.sleep(1)
#Name
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/input').send_keys(naam)
#Klas
if 'a' in klas:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/label/input').click()
elif 'b' in klas:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/label/input').click()
elif 'c' in klas:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/label/input').click()
elif 'd' in klas:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div/label/input').click()
else:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[5]/div/label/input').click()
#Niveau
if 'vwo' in niveau:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/label/input').click()
elif 'havo' in niveau:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/label/input').click()
else:
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div/label/input').click()
#Week1
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div/input').send_keys(week1)
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[2]/div/div/input').send_keys(week12)
#Week2
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div/input').send_keys(week2)
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[7]/div/div[2]/div/div/input').send_keys(week22)
#Week3
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[8]/div/div[2]/div/div/input').send_keys(week3)
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[9]/div/div[2]/div/div/input').send_keys(week32)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button').click()