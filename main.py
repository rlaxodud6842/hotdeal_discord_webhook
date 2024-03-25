import datetime
import requests
import pomppu as p

discord_url = "웹훅 주소"
# 디스코드 채널로 메세지 전송

pp = p.Pomppu()
qa = p.Quasar()
ac = p.Aca()
def discord_send_message():
    message = {"content": f"{pp.get_string() +"\n" + qa.get_string() +"\n" + ac.get_string()}"}
    requests.post(discord_url, data=message)

discord_send_message()


