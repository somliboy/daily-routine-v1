import json
import os
import subprocess

STATE_FILE = "state.json"
PREV_STATE_FILE = "memory/prev_state.json"

def load_json(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def check_state_change():
    current_state = load_json(STATE_FILE)
    previous_state = load_json(PREV_STATE_FILE)

    if previous_state is None:
        print("[🆕 최초 실행] 이전 상태 없음 → 이미지 생성 시작")
        save_json(PREV_STATE_FILE, current_state)
        return True

    if current_state != previous_state:
        print("[🔁 상태 변화 감지됨] 이미지 생성 시작")
        save_json(PREV_STATE_FILE, current_state)
        return True
    else:
        print("[✅ 변화 없음] 동일 상태 유지 중")
        return False

if __name__ == "__main__":
    if check_state_change():
        print("[🎨 이미지 생성 스크립트 실행 중...]")
        subprocess.run(["python", "generate_ara_from_state.py"])
