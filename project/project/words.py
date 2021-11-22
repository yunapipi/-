# サイトを参照するために必要
import requests
from bs4 import BeautifulSoup
import time
import random
import os
import requests
import urllib.parse

def main():
    """
    スクレイピングして問題を作成、ファイルに保存
    """
    # サイトから必要な要素を抽出
    page_url = "https://hangeuls.com/word/0001.html"
    r = requests.get(page_url)
    # 文字化けしてしまっているので直す
    # いま表示されている文字コードを元のサイトで使われていた文字コードに変更
    # print(r.encoding) # 文字化け
    # print(r.apparent_encoding) # サイトの文字コード
    r.encoding = r.apparent_encoding
    # return以降の分は実行されない
    # return
    soup = BeautifulSoup(r.text, features="html.parser")
    # print(soup)
    # return
    # tdに必要な情報が書かれていたのでtdを抽出する
    td_list = soup.find_all(class_ = ["jp", "kr"])
    # print(td_list)
    # return
    # tdタグの中身をリストに入れる
    td_values = [x.text for x in td_list]
    # print(td_values)
    # リストの中をさらに分ける
    splited_list = []
    for index in range(0, len(td_values), 3):
        # print(index)
        # print(td_values[index])
        # print(td_values[index: index + 3])
        a = td_values[index: index + 3]
        # リストにリストが追加された
        splited_list.append(a)
        # print(splited_list)
    # データに書き込む
    with open("words_number.text", "w") as f:
        for value in splited_list:
            f.write("{},{},{}\n".format(value[0],value[1],value[2]))
            # f.write(value[0] + "\n")
            # f.write(value[1] + "\n")
            # f.write(value[2] + "\n")

    page_url = "https://hangeuls.com/word/0031.html"
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, features="html.parser")
    td_list = soup.find_all(class_ = ["jp", "kr"])
    td_values = [x.text for x in td_list]
    splited_list = []
    for index in range(0, len(td_values), 3):
        # print(index)
        # print(td_values[index])
        # print(td_values[index: index + 3])
        a = td_values[index: index + 3]
        # リストにリストが追加された
        splited_list.append(a)
        # print(splited_list)
    # データに書き込む
    with open("words_move.text", "w") as f:
        for value in splited_list:
            f.write("{},{},{}\n".format(value[0],value[1],value[2]))

    page_url = "https://hangeuls.com/word/0032.html"
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, features="html.parser")
    td_list = soup.find_all(class_ = ["jp", "kr"])
    td_values = [x.text for x in td_list]
    splited_list = []
    for index in range(0, len(td_values), 3):
        # print(index)
        # print(td_values[index])
        # print(td_values[index: index + 3])
        a = td_values[index: index + 3]
        # リストにリストが追加された
        splited_list.append(a)
        # print(splited_list)
    # データに書き込む
    with open("words_live.text", "w") as f:
        for value in splited_list:
            f.write("{},{},{}\n".format(value[0],value[1],value[2]))

    page_url = "https://hangeuls.com/word/0033.html"
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, features="html.parser")
    td_list = soup.find_all(class_ = ["jp", "kr"])
    td_values = [x.text for x in td_list]
    splited_list = []
    for index in range(0, len(td_values), 3):
        # print(index)
        # print(td_values[index])
        # print(td_values[index: index + 3])
        a = td_values[index: index + 3]
        # リストにリストが追加された
        splited_list.append(a)
        # print(splited_list)
    # データに書き込む
    with open("words_emotion.text", "w") as f:
        for value in splited_list:
            f.write("{},{},{}\n".format(value[0],value[1],value[2]))

    page_url = "https://hangeuls.com/word/0003.html"
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, features="html.parser")
    td_list = soup.find_all(class_ = ["jp", "kr"])
    td_values = [x.text for x in td_list]
    splited_list = []
    for index in range(0, len(td_values), 3):
        # print(index)
        # print(td_values[index])
        # print(td_values[index: index + 3])
        a = td_values[index: index + 3]
        # リストにリストが追加された
        splited_list.append(a)
        # print(splited_list)
    # データに書き込む
    with open("words_day.text", "w") as f:
        for value in splited_list:
            f.write("{},{},{}\n".format(value[0],value[1],value[2]))

    page_url = "https://hangeuls.com/word/0006.html"
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, features="html.parser")
    td_list = soup.find_all(class_ = ["jp", "kr"])
    td_values = [x.text for x in td_list]
    splited_list = []
    for index in range(0, len(td_values), 3):
        # print(index)
        # print(td_values[index])
        # print(td_values[index: index + 3])
        a = td_values[index: index + 3]
        # リストにリストが追加された
        splited_list.append(a)
        # print(splited_list)
    # データに書き込む
    with open("words_animal.text", "w") as f:
        for value in splited_list:
            f.write("{},{},{}\n".format(value[0],value[1],value[2]))




if __name__ == "__main__":
    main()