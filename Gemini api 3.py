from google.cloud import aiplatform

# 初始化 AI Platform
aiplatform.init(project='YOUR_PROJECT_ID', location='YOUR_LOCATION')

# 定義提示
prompt = """
Patient: Hello, I have a headache and a sore throat.
Robot: Hello! I'm here to help. How long have you been experiencing these symptoms?
Patient: For about three days now.
Robot: Do you have any other symptoms, like fever or cough?
Patient: Yes, I have a slight fever and a dry cough.
Robot: Thank you for the information. Based on your symptoms, 
it sounds like you might have a viral infection. 
It's important to stay hydrated and get plenty of rest. 
If your symptoms worsen or you have trouble breathing, please seek medical attention immediately. 
Is there anything else I can help you with?
"""

# 設定文本生成模型的參數
params = {
    "temperature": 0.7,
    "max_output_tokens": 150
}

# 創建一個客戶端
client = aiplatform.gapic.PredictionServiceClient()

# 輸入模型名稱
model_name = client.endpoint_path("YOUR_PROJECT_ID", "YOUR_LOCATION", "YOUR_MODEL_ID")

# 準備請求
request = {
    "endpoint": model_name,
    "instances": [{"content": prompt}],
    "parameters": params
}

# 發送請求
response = client.predict(request=request)

# 輸出生成的回應
print(response)
