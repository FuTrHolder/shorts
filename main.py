```python
import os, base64

if os.getenv("YOUTUBE_TOKEN_JSON"):
    with open("token.json", "wb") as f:
        f.write(base64.b64decode(os.getenv("YOUTUBE_TOKEN_JSON")))
```
```python
from agents.agent_d import run_pipeline

if __name__ == "__main__":
    run_pipeline("미국 증시")
```
