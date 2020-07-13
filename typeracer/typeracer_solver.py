from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from pyautogui import typewrite

#chromedriverは[https://chromedriver.chromium.org/downloads]からダウンロード
driver = webdriver.Chrome('./chromedriver')

#入力する文字列がバラバラに配置されているため，番号で並び替えるための番号を抽出する正規表現
pattern =re.compile(r'[0-9]+')

#問題のページを開く
driver.get('http://challenge.rgbsec.xyz:8973/')
time.sleep(3);

#問題のスタートボタンを押す
driver.find_element_by_xpath('/html/body/div/a').click()
time.sleep(6);

#spanタグに単語が入っているためspanタグを抽出
spans = driver.find_elements_by_tag_name('span')
#空の辞書を作成
dic={}
for span in spans:
    try:
        #style属性に番号が割振られていれば，それをキーにして単語を格納．
        dic[int(pattern.search(span.get_attribute("style")).group())]=span.text
    except(AttributeError):
        None
#print('len(dic):'+str(len(dic)))
text=''
#単語を並び替えて文字列を作成．
for i in range(len(dic)):
    text=text+dic[i]
print(text[:-1])
#typewriteでkeyEventを発生させる．（seleniumのkey_sendsではうまくいかなかったため．）
typewrite(text[:-1])
