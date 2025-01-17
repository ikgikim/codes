import os
from moviepy.editor import ImageSequenceClip, concatenate_videoclips
from moviepy.video.fx.all import fadein, fadeout

# 현재 스크립트가 위치한 폴더 경로
folder_path = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트의 경로
image_files = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg'))]

# 이미지 클립 생성
clips = []
for img in image_files:
    clip = ImageSequenceClip([img], fps=60)  # 30fps로 설정
    clip = clip.set_duration(4)  # 각 이미지의 지속 시간을 3초로 설정
    clip = fadein(clip, 0.7)  # 0.7초 동안 페이드 인
    clip = fadeout(clip, 0.7)  # 0.7초 동안 페이드 아웃
    clips.append(clip)

# 모든 클립을 연결
final_clip = concatenate_videoclips(clips, method="compose")

# 최종 비디오 파일로 저장
final_clip.write_videofile('output_video.mp4', codec='libx264', fps=30)
