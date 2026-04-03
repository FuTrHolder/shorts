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
