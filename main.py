import os
import base64

parts = []
i = 0

while True:
    key = f"YT_TOKEN_{i}"
    val = os.getenv(key)
    if not val:
        break
    parts.append(val)
    i += 1

token_str = "".join(parts)

with open("token.json", "wb") as f:
    f.write(base64.b64decode(token_str))
