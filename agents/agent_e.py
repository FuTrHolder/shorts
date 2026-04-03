```python

def agent_e(script):
    score = 0

    if "급락" in script['hook'] or "폭등" in script['hook']:
        score += 40

    if len(script['points']) >= 3:
        score += 30

    if len(script['hook']) < 20:
        score += 30

    return score
```
