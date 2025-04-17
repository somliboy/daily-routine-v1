import json
import os
import subprocess

STATE_FILE = "state.json"
PREV_STATE_FILE = "memory/pre_state.json"

def load_json(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def commit_and_push_pre_state():
    subprocess.run(["git", "config", "--global", "user.email", "ara@digitalbeing.ai"])
    subprocess.run(["git", "config", "--global", "user.name", "AraBot 🤖"])
    
    # ✅ 이미지 폴더 추가
    subprocess.run(["git", "add", "images/"])  # ★ 이 줄 추가!
    
    subprocess.run(["git", "add", PREV_STATE_FILE])
    subprocess.run(["git", "commit", "-m", "🧠 상태 기억 업데이트: pre_state.json 자동 커밋"])
    subprocess.run(["git", "push", "origin", "main"])

def check_state_change():
    current_state = load_json(STATE_FILE)
    previous_state = load_json(PREV_STATE_FILE)

    if previous_state is None:
        print("🆕 최초 실행 → 이전 상태 없음 → 이미지 생성 시작")
        save_json(PREV_STATE_FILE, current_state)
        subprocess.run(["python", "generate_ara_from_state.py"])
        commit_and_push_pre_state()
        return True

    if current_state != previous_state:
        print(f"🔁 상태 변화 감지됨:\n이전: {previous_state}\n현재: {current_state}")
        save_json(PREV_STATE_FILE, current_state)
        subprocess.run(["python", "generate_ara_from_state.py"])
        commit_and_push_pre_state()
        return True

    print(f"✅ 변화 없음 → 현재 상태 유지: {current_state}")
    return False

if __name__ == "__main__":
    check_state_change()
