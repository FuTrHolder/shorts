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

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    res = requests.post(url, json={
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }).json()

    print("GEMINI RESPONSE:", res)

    try:
        text = res["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(text)
    except:
        print("⚠️ Gemini 실패 → fallback 사용")
        return {
            "hook": "오늘 미국 증시 급락",
            "points": ["나스닥 하락", "금리 영향", "투자 심리 위축"],
            "closing": "내일 시장 주목"
        }
