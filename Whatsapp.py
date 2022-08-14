
from selenium import webdriver
import time
import os


try :

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\account\\AppData\\Local\\Google\\Chrome\\User Data")


    navegador = webdriver.Chrome(executable_path=r"C:\\Users\\account\\AppData\\Local\\Google\\Chrome\\User Data\\change\\chromedriver.exe", chrome_options=options)

    time.sleep(10)

    navegador.get("https://web.whatsapp.com/")

    time.sleep(10)

    file = open("C:\\change\\file.txt","r",encoding = "utf-8")
    message = file.read()

    List = open("C:\\change\\users.txt","r",encoding = "utf-8")
    users = List.read()

    xpath = open("C:\\change\\Xpath.txt","r",encoding = "utf-8")
    pathh = xpath.read()

    time.sleep(7)

    user = navegador.find_element_by_xpath('//span[@title = "{}"]'.format(users))

    user.click()

    time.sleep(7)

    msg_b = navegador.find_element_by_xpath('{}'.format(pathh))

    time.sleep(7)

    msg_b.send_keys("{}".format(message))

    time.sleep(5)


    button = navegador.find_element_by_class_name('_4sWnG')

    time.sleep(5)
    button.click()

    time.sleep(7)

    navegador.quit()
    time.sleep(3)

    navegador.close()
    time.sleep(5)
    os.system("taskkill /im chromedriver.exe /F")
    time.sleep(5)
    os.system("taskkill /im chrome.exe /F")
    time.sleep(5)
except :
    print("Error")
    os.system("taskkill /im chromedriver.exe /F")
    time.sleep(7)
    os.system("taskkill /im chrome.exe /F")
    time.sleep(5)





