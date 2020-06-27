"""
特許情報プラットフォームから特許の発明名称をとってくるプログラム
"""
# coding:utf-8
import os
import time

import requests

from selenium import webdriver


def scroll(driver):
    """
    ページを下までスクロールする。
    """
    html01 = driver.page_source
    while 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        html02 = driver.page_source
        if html01 != html02:
            html01 = html02
        else:
            break
def main():
    """
    特許情報プラットフォームにて任意の検索項目にヒットする
    特許の発明名称を取得する
    """
    path = os.getcwd()  # 現在のディレクトリを取得
    # ドライバーを設定
    driver = webdriver.Chrome(path + '\\chromedriver')
    # 特許情報プラットフォームにアクセス
    driver.get('https://www.j-platpat.inpit.go.jp/')

    # 検索するワードの設定
    print('What are you search?')
    serach_word = input()
    # 作成するファイル名の設定
    print('please type a file name')
    file_name = input()

    time.sleep(2)
    driver.find_element_by_name('s01_srchCondtn_txtSimpleSearch').click()
    driver.find_element_by_name('s01_srchCondtn_txtSimpleSearch').send_keys(serach_word)
    driver.find_element_by_name('s01_srchBtn_btnSearch').click()
    time.sleep(5)

    # ページスクロール
    scroll(driver)

    # 検索結果に合致する物の最大のNoを取得
    id_str = driver.find_elements_by_id('patentUtltyIntnlSimpleBibLst_tableView_numberArea')[-1].text
    id_num = int(id_str)

    words = []
    for i in range(id_num):
        word = driver.find_element_by_id('patentUtltyIntnlSimpleBibLst_tableView_invenName{}'.format(i)).text
        words.append(word)
        print(word)
    print(words)

    # テキストファイルを作成
    with open(file_name, 'w') as f:
        f.write('\n'.join(words))


if __name__ == "__main__":
    main()
