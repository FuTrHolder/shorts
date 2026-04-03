from utils.youtube import upload_youtube

def agent_c(video_path, title):
    return upload_youtube(video_path, title, "자동 생성 영상")
