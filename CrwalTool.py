from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 옵션 생성
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

time.sleep(1)

class Acalive:
    def __init__(self):
        self.URL = 'https://arca.live/b/hotdeal'
        self.before_array = [True]
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

        set1 = set(parsed_arr)
        set2 = set(self.before_array)

        parsed_arr = set1 - set2

        # 이전 배열 받아서

        return parsed_arr

    def get_string(self):
        string = "아카라이브 Hot Deal Top 5\n"
        arr = self.parsing()
        for item in arr:
            string += item + "\n"
        # print(string)
        return string
