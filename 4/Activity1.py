import requests
from config import hf_api_key

def classify_text(text):
    api_url="https://api-inference.huggingface.co/models/distilbert-based-uncased-finetuned-sst-2-english"
    headers={"authorisation": f"vearer {hf_api_key}"}
    payload={"input":text}
    response=requests.post(api_url, headers=headers , json=payload)
    return response.json()
result=classify_text(" I love using hugging face api")
print(result)