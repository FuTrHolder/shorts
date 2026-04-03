from utils.youtube import upload_youtube


def agent_c(video, title):
    return upload_youtube(video, title, "자동 생성 영상")

