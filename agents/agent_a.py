import requests
import os
import json

def agent_a(topic):
    api_key = os.getenv("GEMINI_API_KEY")

    prompt = f"""
너는 미국 증시 전문가야.

주제: {topic}

조건:
- 한국어
- 유튜브 쇼츠용
- 30초 분량
- 강한 후킹 포함

JSON으로만 출력:
{{
  "hook": "",
  "points": ["", "", ""],
  "closing": ""
}}
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    res = requests.post(url, json={
        "contents": [{"parts": [{"text": prompt}]}]
    }).json()

    text = res["candidates"][0]["content"]["parts"][0]["text"]

    try:
        return json.loads(text)
    except:
        # JSON 깨질 경우 기본값
        return {
            "hook": "오늘 미국 증시 급락 상황",
            "points": ["나스닥 하락", "금리 영향", "투자 심리 위축"],
            "closing": "내일 시장이 중요합니다"
        }
