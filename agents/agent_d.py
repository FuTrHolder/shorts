```python
from agents.agent_a import agent_a
from agents.agent_b import agent_b
from agents.agent_c import agent_c
from agents.agent_e import agent_e


def run_pipeline(topic):
    for i in range(3):
        print(f"Attempt {i+1}")

        script = agent_a(topic)
        score = agent_e(script)

        if score >= 80:
            video = agent_b(script)
            video_id = agent_c(video, script['hook'])
            print("Uploaded:", video_id)
            return

        topic += " 충격"

    print("FAILED")
```
