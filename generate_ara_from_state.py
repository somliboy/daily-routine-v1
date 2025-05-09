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

# 이미지 저장 (timestamp + latest.png 덮어쓰기)
try:
    res = requests.get(image_url)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"ara_{timestamp}.png"
    
    output_dir = Path("images")
    output_dir.mkdir(exist_ok=True)
    
    # ① 타임스탬프 버전 저장
    with open(output_dir / filename, "wb") as f:
        f.write(res.content)

    # ② latest.png 덮어쓰기
    with open(output_dir / "latest.png", "wb") as f:
        f.write(res.content)

    print(f"✅ 이미지 저장 완료: {filename} (아카이빙)")
    print("✅ 최신 이미지 업데이트 완료: latest.png")

except Exception as e:
    print("❌ 이미지 다운로드 실패:", e)

