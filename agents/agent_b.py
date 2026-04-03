import os
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"

from moviepy.editor import TextClip, ColorClip, CompositeVideoClip, concatenate_videoclips

def make_clip(text):
    txt = TextClip(
        text,
        fontsize=70,
        color="white",
        size=(720, 1280),
        method="caption"
    ).set_duration(2)

    bg = ColorClip(size=(720,1280), color=(0,0,0)).set_duration(2)

    return CompositeVideoClip([bg, txt.set_position("center")])

def agent_b(script):
    clips = []

    clips.append(make_clip(script["hook"]))

    for p in script["points"]:
        clips.append(make_clip(p))

    clips.append(make_clip(script["closing"]))

    final = concatenate_videoclips(clips)

    output_path = "shorts.mp4"
    final.write_videofile(output_path, fps=24)

    return output_path
