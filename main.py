from selenium import webdriver
import time
import requests

URL = "http://www.higherlowergame.com/"
DELAY = 2

print("Opening Browser...")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("driver\chromedriver.exe", options=options)
print("Fetching URL..")
driver.get(URL)

print("Starting Game...")
time.sleep(DELAY)
start_btn = driver.find_element_by_class_name("game-button--start")
start_btn.click()
time.sleep(DELAY)

while(True):

    left = driver.find_element_by_xpath(
        '//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[1]/div/div[1]/p[1]')
    title_left = left.text
    title_left = title_left.replace('“', "")
    title_left = title_left.replace('”', "")

    right = driver.find_element_by_xpath(
        '//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[2]/div/div[1]/p[1]')
    title_right = right.text
    title_right = title_right.replace('“', "")
    title_right = title_right.replace('”', "")

    APIURL = "http://sohamsahare123.pythonanywhere.com/api/v1/resources/data/higherlower/" + \
        title_left+"/"+title_right
    response = requests.get(APIURL)
    answer = response.text

    if(answer == "Higher"):
        btn_H = driver.find_element_by_class_name(
            "term-actions__button--higher").click()
        print("\n{} < {}\n".format(title_left, title_right))
    else:
        btn_L = driver.find_element_by_class_name(
            "term-actions__button--lower").click()
        print("\n{} > {}\n".format(title_left, title_right))

    time.sleep(DELAY+3)

driver.close()
