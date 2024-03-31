import requests
import CrwalTool as aca

import schedule

discord_url = "https://discord.com/api/webhooks/1221802874884063252/c_1frV36Yt2a-qEVLAG6hO66OI-oBL_WAoj4tlsvA0lNZMOp1AGSL_6fxwH3MW1C2QtO"
# 디스코드 채널로 메세지 전송

ac = aca.Acalive()
def discord_send_message():
    message = {"content": f"{ac.get_string()}"}
    requests.post(discord_url, data=message)

discord_send_message()

schedule.every(1).minutes.do(discord_send_message)
while True:
    schedule.run_pending()


# 1시간분마다 크롤링.
# 크롤링에 있는거랑 비교해서 달라진거 있으면 올리고, 없으면 대기
