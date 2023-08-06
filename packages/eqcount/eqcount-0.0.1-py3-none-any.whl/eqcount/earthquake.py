from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


def result(driver):
    #ウィンドウ非表示設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    #ChromeDriverのパスを引数に指定しChromeを起動
    driver = webdriver.Chrome(driver ,options=options)

    #ページが完全にロードされるまで最大で5秒間待つよう指定
    driver.set_page_load_timeout(5)

    try:
    #指定したURLに遷移する
        driver.get("http://www.data.jma.go.jp/svd/eqdb/data/shindo/index.html")
    except:
    #ページが完全にロードされるまで5秒以上かかる場合は以下を出力
        print("time out!")
        
    #期間10年間設定
    driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/fieldset/p[1]/button[8]").click()

    #震度選択震度3以上
    driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/fieldset/p[2]/select/option[3]").click()

    #検索
    driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/fieldset/p[1]/button").click()

    #リスト表示
    driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/img[2]").click()

    time.sleep(6)

    #csvダウンロード
    driver.find_element_by_id("outputCsvS").click()
    Alert(driver).accept()

    time.sleep(5)


    df = pd.read_csv('地震リスト.csv')
    #グラフ描画
    plt.style.use('ggplot')
    x = df['震央地名'].value_counts().head(30).index
    y= df['震央地名'].value_counts().head(30)

    plt.figure(figsize=(20,15))
    plt.bar(x, y)
    plt.xlabel('震央地')
    plt.ylabel('回数')
    plt.title('震央地と回数')
    plt.xticks(rotation=90)
    plt.show()