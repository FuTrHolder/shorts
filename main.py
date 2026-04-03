```python
import os, base64

if os.getenv("YOUTUBE_TOKEN_JSON"):
    with open("token.json", "wb") as f:
        f.write(base64.b64decode(os.getenv("YOUTUBE_TOKEN_JSON")))
```
