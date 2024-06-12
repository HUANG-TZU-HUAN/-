import os

import google.generativeai as genai

os.environ["AIzaSyC0xHIJ922U7TofueVkuv2QwOp_pjId1Jc"] = 'AIzaSyC0xHIJ922U7TofueVkuv2QwOp_pjId1Jc'
genai.configure(api_key=os.environ["AIzaSyC0xHIJ922U7TofueVkuv2QwOp_pjId1Jc"])

model = genai.GenerativeModel('gemini-1.5-flash')

# 定義對話腳本提示工程
initial_prompt = """
患者：你好，我頭痛並且喉嚨痛。
機器人：你好！你能告訴我你這些症狀已經持續多久了嗎？
患者：大約三天了。
機器人：謝謝。你有其他症狀嗎，像發燒或咳嗽？
患者：是的，我有輕微的發燒和乾咳。
機器人：根據你的症狀，聽起來你可能有病毒感染。我建議你去看一下內科。保持水分補充和充足休息很重要。如果你的症狀惡化或呼吸困難，請立即尋求醫療協助。
你想要預約內科嗎？
"""

registration_prompt = """
患者：是的，我想預約。
機器人：太好了。我們來幫你註冊一下。請提供你的全名和出生日期。
患者：我的名字是約翰·多，出生日期是1990年1月1日。
機器人：謝謝你，約翰。我已經為你在一般醫學科預約了一個時間。你的預約安排在明天上午10點。請提前15分鐘到達，完成任何必要的文件。
"""

pre_appointment_reminder_prompt = """
機器人：你好約翰，這是提醒你明天上午10點與一般醫學科的預約。請確保帶上你的身份證和任何醫療記錄。提前15分鐘到達，以完成任何必要的文件。
"""

post_appointment_follow_up_prompt = """
機器人：嗨約翰，我希望你去一般醫學科的看診進展順利。這是你的醫生給出的一些後續指示：

保持水分補充，並充足休息。
按照指示服用處方藥物。
監控你的症狀，如果惡化，立即尋求醫療協助。
你想預約後續的掛號嗎？
"""

follow_up_appointment_prompt = """

患者：是的，我想預約一個後續的掛號。
機器人：當然。你什麼時候方便再來進行後續的掛號？
患者：下週一對我來說可以。
機器人：我已經為你安排了下週一上午10點的後續掛號。你將在預約前一天收到提醒。注意身體，祝你早日康復！
"""

health_management_prompt = """

機器人：作為你持續健康管理的一部分，這裡有一些建議：

保持均衡的飲食，並保持水分補充。
定期運動。
確保充足的睡眠。
如果你有任何問題或需要進一步協助，請隨時聯繫我們。我們樂意幫助！
"""

# 發送請求並輸出結果
response = model.generate_content(initial_prompt)
print(response.text)

response = model.generate_content(registration_prompt)
print(response.text)

response = model.generate_content(pre_appointment_reminder_prompt)
print(response.text)

response = model.generate_content(post_appointment_follow_up_prompt)
print(response.text)

response = model.generate_content(follow_up_appointment_prompt)
print(response.text)

response = model.generate_content(health_management_prompt)
print(response.text)
