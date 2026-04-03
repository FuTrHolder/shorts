from moviepy.editor import TextClip, ColorClip, CompositeVideoClip, concatenate_videoclips

def agent_b(script):
    lines = [script["hook"]] + script["points"] + [script["closing"]]

    clips = []

    for line in lines:
        txt = TextClip(line, fontsize=70, color="white", size=(720,1280), method="caption")
        txt = txt.set_duration(3).set_position("center")

        bg = ColorClip(size=(720,1280), color=(0,0,0), duration=3)

        clip = CompositeVideoClip([bg, txt])
        clips.append(clip)

    final = concatenate_videoclips(clips)
    final.write_videofile("output.mp4", fps=30)

    return "output.mp4"
