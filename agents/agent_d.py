from agents.agent_a import agent_a
from agents.agent_b import agent_b
from agents.agent_c import agent_c
from agents.agent_e import agent_e

def run_pipeline(topic):
    print("PIPELINE START")

    for i in range(3):
        print(f"Attempt {i+1}")

        script = agent_a(topic)
        print("SCRIPT:", script)

        score = agent_e(script)
        print("SCORE:", score)

        if score >= 80:
            print("PASS → 영상 생성")
            video = agent_b(script)

            print("UPLOAD 시작")
            video_id = agent_c(video, script["hook"])

            print("Uploaded:", video_id)
            return

        topic += " 충격"

    print("FAILED")
