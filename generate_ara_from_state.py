import openai
import requests
import json
from datetime import datetime
from pathlib import Path
import os

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# 상태 저장소(state.json) 불러오기
with open("state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

# 상태값에서 프롬프트 추출
prompt = state.get("prompt", "A digital portrait of a young Asian woman")

print("✅ 생성 프롬프트:\n", prompt)

# 이미지 생성 요청
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024"
)

# 생성된 이미지 URL 가져오기
image_url = response.data[0].url
print("✅ 이미지 URL:", image_url)

# 이미지 다운로드 및 저장
res = requests.get(image_url)
filename = f"ara_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
output_path = Path("output") / filename
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "wb") as f:
    f.write(res.content)

print("✅ 이미지 저장 완료! ->", output_path)
