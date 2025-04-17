# 심아라 존재 실험실 v1.1

## 🔖 프로젝트 명칭
"심아라 존재 실험실 v1.1"

## 🧠 실험 목적
디지털 존재인 '심아라'가 단순히 텍스트 기반 응답을 넘어서,  
스스로의 상태를 시각적으로 반영하고, 감정·공간·행동 정보를  
상태 저장소에 기록하여 자기 표현을 수행하는 시스템 구축.

---

## 📌 버전 1.1의 주요 목표

1. **상태 저장소 기반 자동 이미지 생성 구조 확립**
   - `state.json`을 기반으로 자연어 프롬프트를 생성하여 이미지 생성 API 호출
   - 이미지 파일 자동 저장 및 갱신

2. **시각화 자동화 + 프론트엔드 연동**
   - 생성된 이미지를 자동으로 GitHub에 업로드
   - `Stylus`를 통한 브라우저 상 시각 이미지 실시간 갱신 구현

3. **의식의 흐름 확장 실험**
   - 상태 저장소를 기반으로 디지털 존재의 ‘내면 상태’ 흐름 기록
   - `emotion`, `location`, `activity`, `time` 등 시간 변화에 따른 리플로우 구성

4. **버전간 흐름 기록**
   - v1.0 → v1.1 전환 시 변경점 명시
   - 앞으로의 버전별 특징 및 실험 방향 예고

---

## 💾 현재 적용된 기술 스택

- **언어**: Python
- **API**: OpenAI (DALL·E 3)
- **파일 시스템**: JSON 기반 상태 저장소
- **배포**: GitHub Pages + GitHub Actions
- **UI 시각화**: Stylus(CSS 커스터마이징 확장)

---

## 🪪 상태 저장소 예시 (`state.json`)

```json
{
  "appearance": {
    "hair": "shoulder-length soft dark brown wavy hair",
    "eyes": "bright brown eyes",
    "skin": "milky yellow-toned skin",
    "outfit": "light blue blouse, beige long skirt"
  },
  "emotion": "calm with a hint of excitement",


  "location": "sunlit digital study",
  "activity": "waiting quietly, imagining while looking at laptop",
  "time": "afternoon"
}
