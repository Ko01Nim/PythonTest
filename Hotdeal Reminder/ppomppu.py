from matplotlib.pyplot import text
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import telegram
import time

ppomppuURL = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
fmkoreaURL = 'https://www.fmkorea.com/hotdeal'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url=fmkoreaURL)

driver.implicitly_wait(time_to_wait=10)

fmkorea_send_messages = []

try :
    while True : 
            ppomppu_titles = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
            ppomppu_urls = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')
            
            fmkorea_titles = driver.find_elements(By.CSS_SELECTOR, '#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li:nth-child(1) > div > h3 > a')
            fmkorea_urls = driver.find_elements(By.CSS_SELECTOR, '#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li:nth-child(1) > div > a:nth-child(2)')
        
            fmkorea_message = ""
            
            #message = titles[0].text + "\n" + urls[0].get_attribute('href')
            fmkorea_message = fmkorea_titles[0].text + "\n" + fmkorea_urls[0].get_attribute('href')
            
            if fmkorea_message not in fmkorea_send_messages :
                print(fmkorea_message)
                print('===============================================')
                fmkorea_send_messages.append(fmkorea_message)
                token = '5757209381:AAFzs97HU7iZjvR_7V5dCaFA9zZHrz0NMPU'
                id = '5758273485'
                    
                bot = telegram.Bot(token)
                bot.sendMessage(chat_id=id, text=fmkorea_message)
                    
            time.sleep(60.0 * 1)

except KeyboardInterrupt:
    print('Pause')    