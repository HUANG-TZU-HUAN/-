import json

import requests

api_key ="AIzaSyC0xHIJ922U7TofueVkuv2QwOp_pjId1Jc"  # 将此处替换为您的实际API密钥
url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=AIzaSyC0xHIJ922U7TofueVkuv2QwOp_pjId1Jc'
headers = {'Content-Type': 'application/json'}

# 定义诊所服务机器人和病患的对话内容，保持不变
data = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": "我最近感覺胸口有點悶，應該看哪個科別？"}]
        },
        {
            "role": "model",
            "parts": [{"text": "根據您的症狀描述，建議您先掛號內科進行初步檢查。是否需要我幫您掛號？"}]
        },
        {
            "role": "user",
            "parts": [{"text": "好的，請幫我掛號。"}]
        },
        {
            "role": "model",
            "parts": [{"text": "您的掛號已完成，請於明天上午9點前往內科診所看診。"}]
        },
        {
            "role": "user",
            "parts": [{"text": "看診前有什麼需要注意的嗎？"}]
        },
        {
            "role": "model",
            "parts": [{"text": "請您在看診前保持空腹，以便進行必要的檢查。看診後，醫生會根據檢查結果給出進一步的建議。"}]
        },
        {
            "role": "user",
            "parts": [{"text": "看診後我應該怎麼做？"}]
        },
        {
            "role": "model",
            "parts": [{"text": "看診後，請根據醫生的建議進行後續的健康管理。如果需要回診，我會提前提醒您預約回診時間。"}]
        },
        {
            "role": "user",
            "parts": [{"text": "好的，謝謝你！"}]
        },
        {
            "role": "model",
            "parts": [{"text": "不客氣，祝您早日康復！如果有任何問題，隨時聯繫我。"}]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print(f"response status_code: {response.status_code}")
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
