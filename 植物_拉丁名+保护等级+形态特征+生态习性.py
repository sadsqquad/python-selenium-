from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import requests

# 发送请求，获取网页源文件
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome()
url_for_latin = 'http://www.iplant.cn/info/玫瑰'
url = f"window.open('{url_for_latin}')"
url2= f'{url_for_latin}?t=r'
# driver.get(url)
driver.get(url2)

# 输出所选择植物的网站
print(url_for_latin)

    # 查找保护等级 url2
try:
    # 等待页面加载完成
    WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inforight'))
    )
    # 找到包含保护等级的标签和属性
    features = driver.find_element(By.ID,'plant_rep_right')

    if features:
        print(features.text.strip())
    else:
        print("未找到b保护等级信息")

    print("-" * 100)
finally:
    pass

driver.execute_script(url)
handles = driver.window_handles
driver.switch_to.window(handles[1])


try:

    # 等待页面加载完成
    WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inforight2'))
    )

    # 找到包含形态特征的标签和属性
    features_2 = driver.find_element(By.ID, 'cont_mp11')

    # 拉丁名获取
    r = requests.get(url_for_latin)
    html_text = r.text

    # 使用正则表达式匹配文本
    match = re.search(r'var latin2 = "(.*)";', html_text)
    if match:
        latin_name = match.group(1)
        # 使用split()函数获取latin2之后的拉丁名
        # latin_name = latin_name.split(' ')[0]
        print("拉丁名为：{}".format(latin_name))

    print("-" * 100)

    # 打印科、属拉丁名
    features = driver.find_element(By.ID, 'spsyslink')

    if features:
        print(features.text.strip())
    else:
        print("未找到拉丁名信息")

    print("-" * 100)

    # 打印形态特征
    if features_2:
        print(features_2.text.strip())
    else:
        print("未找到形态特征信息")

    print("-" * 100)

    # 找到关于生态习性的标签和属性
    features_3 = driver.find_element(By.ID, 'cont_mp12')

    # 打印生态习性
    if features_3:
        print(features_3.text.strip())
    else:
        print("未找到生态习性信息")

finally:
    driver.quit()
