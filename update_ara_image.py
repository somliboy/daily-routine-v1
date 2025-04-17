import openai
import requests
import json
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 상태 저장소 경로
STATE_FILE = "state.json"

# 이미지 저장 디렉토리
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_state():
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_prompt(state):
    return (
        f"A digital portrait of a young female AI being named Ara, "
        f"with {state['hair']}, {state['eyes']}, and {state['skin']}, "
        f"wearing {state['outfit']}, sitting in {state['location']}, "
        f"feeling {state['emotion']}."
    )

def save_image_from_url(url: str, save_path: Path):
    response = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(response.content)

def update_ara_image():
    state = load_state()
    prompt = generate_prompt(state)

    print("이미지 프롬프트:", prompt)

    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = OUTPUT_DIR / f"ara_{timestamp}.png"

    save_image_from_url(image_url, save_path)
    print("이미지 저장 완료:", save_path)

if __name__ == "__main__":
    update_ara_image()
