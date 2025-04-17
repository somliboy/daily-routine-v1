import openai
import requests
from datetime import datetime
from pathlib import Path
import json
import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# state.json 불러오기
with open("state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

# 이미지 프롬프트 만들기
prompt = (
    f"A digital portrait of a young female AI being named Ara, "
    f"with {state['hair']}, {state['eyes']}, and {state['skin']}, "
    f"wearing {state['outfit']}, sitting in {state['location']}, "
    f"feeling {state['emotion']}."
)

print("프롬프트:", prompt)

# 이미지 생성
response = openai.images.generate(
    model="dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024"
)

# 이미지 저장
image_url = response.data[0].url
res = requests.get(image_url)

filename = f"ara_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
output_path = Path("output") / filename
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "wb") as f:
    f.write(res.content)

print("이미지 저장 완료:", output_path)
