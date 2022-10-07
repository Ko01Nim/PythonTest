#깃허브
#https://webnautes.tistory.com/1422
#https://copymaster.tistory.com/entry/Web-VS-Code-Git-%EA%B8%B0%EB%8A%A5-%EC%B6%94%EA%B0%80-%EB%B0%8F-History-%EA%B4%80%EB%A6%AC

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

#driver.implicitly_wait(time_to_wait=10)

ppomppu_send_messages = []
fmkorea_send_messages = []

loop_cnt = 1

try :
    token = '5757209381:AAFzs97HU7iZjvR_7V5dCaFA9zZHrz0NMPU'
    id = '5758273485'
    bot = telegram.Bot(token)
            
    while True : 
        #PPOMPPU
        driver.get(url=ppomppuURL)
        ppomppu_titles = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
        ppomppu_urls = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')
        
        ppomppu_message = ""
        
        ppomppu_message = ppomppu_titles[0].text + "\n" + ppomppu_urls[0].get_attribute('href')
        
        if ppomppu_message not in ppomppu_send_messages :
            print('============= PPOMPPU 전송 START =============')
            ppomppu_send_messages.append(ppomppu_message)
            bot.sendMessage(chat_id=id, text=ppomppu_message)
            print(ppomppu_message)
            print('============= PPOMPPU 전송 END =============')
        else :
            print('============= PPOMPPU 전송 내역 없음 =============')
            
        #FMKOREA
        driver.get(url=fmkoreaURL)
        fmkorea_titles = driver.find_elements(By.CSS_SELECTOR, '#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li:nth-child(1) > div > h3 > a')
        fmkorea_urls = driver.find_elements(By.CSS_SELECTOR, '#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li:nth-child(1) > div > a:nth-child(2)')
        
        fmkorea_message = ""
        
        fmkorea_message = fmkorea_titles[0].text + "\n" + fmkorea_urls[0].get_attribute('href')
        
        if fmkorea_message not in fmkorea_send_messages :
            print('============= FMKOREA 전송 START =============')
            fmkorea_send_messages.append(fmkorea_message)
            bot.sendMessage(chat_id=id, text=fmkorea_message)
            print(fmkorea_message)
            print('============= FMKOREA 전송 END =============')
        else :
            print('============= FMKOREA 전송 내역 없음 =============')
            
        print("루프 카운트 : " + str(loop_cnt))     
        loop_cnt = loop_cnt + 1
         
        time.sleep(60.0 * 1)
        
except KeyboardInterrupt:
    print('Pause')    