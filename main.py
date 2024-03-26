import requests
import pomppu as p

import schedule
import time

discord_url = "https://discord.com/api/webhooks/1221802874884063252/c_1frV36Yt2a-qEVLAG6hO66OI-oBL_WAoj4tlsvA0lNZMOp1AGSL_6fxwH3MW1C2QtO"
# 디스코드 채널로 메세지 전송

pp = p.Pomppu()
qa = p.Quasar()
ac = p.Aca()
def discord_send_message():
    message = {"content": f"{pp.get_string() +"\n" + qa.get_string() +"\n" + ac.get_string()}"}
    requests.post(discord_url, data=message)

discord_send_message()
schedule.every(1).minutes.do(discord_send_message)
while True:
    print("반복")
    schedule.run_pending()

