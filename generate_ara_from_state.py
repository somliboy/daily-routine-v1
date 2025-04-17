import openai
import requests
import json
import os
from datetime import datetime
from pathlib import Path

# GitHub Actions에서도 사용 가능하게 환경변수 직접 읽기
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 상태 불러오기
with open("state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

# 프롬프트 구성
appearance = state.get("appearance", {})
emotion = state.get("emotion", "")
location = state.get("location", "")
activity = state.get("activity", "")
time = state.get("time", "")

prompt = (
    f"A digital portrait of a young East Asian woman with "
    f"{appearance.get('hair', '')}, "
    f"{appearance.get('eyes', '')}, and "
    f"{appearance.get('skin', '')}, wearing "
    f"{appearance.get('outfit', '')}, "
    f"{activity} in a {location} during the {time}, "
    f"feeling {emotion}."
)

print("✅ 생성 프롬프트:\n", prompt)

# 이미지 생성
try:
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response["data"][0]["url"]
    print("✅ 이미지 URL:", image_url)
except Exception as e:
    print("❌ 이미지 생성 실패:", e)
    exit(1)

# 이미지 저장
try:
    res = requests.get(image_url)
    filename = f"ara_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    output_path = Path("images") / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(res.content)
    print("✅ 이미지 저장 완료! ->", output_path)
except Exception as e:
    print("❌ 이미지 다운로드 실패:", e)
