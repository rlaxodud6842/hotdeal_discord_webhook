from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(1)

class Pomppu:
    def __init__(self):
        self.URL = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&hotlist_flag=999'

    def crwaling(self):
        driver.get(self.URL)
        time.sleep(2)

        pp_item = driver.find_elements(By.CLASS_NAME, "list_title")
        time.sleep(2)
        return pp_item

    def parsing(self):
        start = 2 #공지를 제외하기 위한 수
        end = 7

        arr = self.crwaling()
        parsed_arr = arr[start:end]
        return parsed_arr

    def get_string(self):
        string = "뽐뿌 Hot Deal Top 5\n"
        arr = self.parsing()
        for i,item in enumerate(arr):
            string += item.text +"\n"

        #print(string)
        return string


class Quasar:
    def __init__(self):
        self.URL = 'https://quasarzone.com/bbs/qb_saleinfo?_method=post&type=&page=1&_token=lCfkQcKEM2zWaP2eL8QQboVOqH8sgxrKpEshZcnL&category=&popularity=N&kind=subject&keyword=&sort=num%2C+reply&direction=DESC'
    def crwaling(self):
        driver.get(self.URL)
        time.sleep(2)

        qa_item = driver.find_elements(By.CLASS_NAME, "ellipsis-with-reply-cnt")
        time.sleep(2)
        return qa_item

    def parsing(self):
        end = 5
        start = 0
        arr = self.crwaling()
        parsed_arr = arr[start:end]
        return parsed_arr

    def get_string(self):
        string = "퀘이사존 Hot Deal Top 5\n"
        arr = self.parsing()
        for i, item in enumerate(arr):
            string += item.text + "\n"

        # print(string)
        return string


class Aca:
    def __init__(self):
        self.URL = 'https://arca.live/b/hotdeal'
    def crwaling(self):
        driver.get(self.URL)
        time.sleep(2)

        item_packet = []

        ac_item = driver.find_elements(By.CLASS_NAME, "title.hybrid-title") #공백은 .으로 공백없이 해줘야하네 각 아이템 이름
        time.sleep(2)

        ac_cost = driver.find_elements(By.CLASS_NAME, "deal-price") #가격
        time.sleep(2)

        ac_deliver = driver.find_elements(By.CLASS_NAME, "deal-delivery")  # 배달비
        time.sleep(2)

        item_packet.append(ac_item)
        item_packet.append(ac_cost)
        item_packet.append(ac_deliver)
        return item_packet

    def merging(self):
        item_list = []
        item_packet = self.crwaling()
        length = len(item_packet[0])
        for i in range(length):
            merged_item = ""
            merged_item += item_packet[0][i].text + "("+item_packet[1][i].text+"/"+item_packet[2][i].text+")"
            item_list.append(merged_item)

        return item_list
        # 두개의 배열을 받아와서
        # 하나에 배열에 합쳐서 하나씩 넣기

    def parsing(self):
        end = 5
        start = 0
        arr = self.merging()
        parsed_arr = arr[start:end]
        return parsed_arr

    def get_string(self):
        string = "아카라이브 Hot Deal Top 5\n"
        arr = self.parsing()
        for item in arr:
            string += item + "\n"
        # print(string)
        return string
