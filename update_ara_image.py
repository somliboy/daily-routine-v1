import openai
import requests
from datetime import datetime
from pathlib import Path
import os

# 시크릿에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# 이미지 생성 프롬프트
prompt = "A digital portrait of a young Asian woman with shoulder-length soft wavy dark brown hair, light brown eyes, and a gentle smile, sitting in a sunny digital study, wearing a light blue blouse and a beige long skirt"

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024"
)

image_url = response.data[0].url
print("Generated image URL:", image_url)

# 이미지 저장
res = requests.get(image_url)
filename = f"ara_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
output_path = Path("output") / filename
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "wb") as f:
    f.write(res.content)

print("이미지 저장 완료! ->", output_path)
