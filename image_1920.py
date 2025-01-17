import os
from PIL import Image

def resize_and_crop_images(folder_path):
    # '변경됨' 하위 폴더 생성
    output_folder = os.path.join(folder_path, '변경됨')
    os.makedirs(output_folder, exist_ok=True)

    # 폴더 내 모든 파일을 확인
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                # 원본 이미지 크기
                original_width, original_height = img.size
                
                # 가로축을 1920으로 리사이즈
                new_width = 1920
                aspect_ratio = original_height / original_width
                new_height = int(new_width * aspect_ratio)
                
                # 이미지 리사이즈
                img = img.resize((new_width, new_height), Image.LANCZOS)
                
                # 세로축이 1080보다 많이 남으면 잘라내기
                if new_height > 1080:
                    excess_height = new_height - 1080
                    crop_top = excess_height // 2
                    crop_bottom = excess_height - crop_top
                    img = img.crop((0, crop_top, new_width, new_height - crop_bottom))
                
                # 최종 이미지 리사이즈
                img = img.resize((1920, 1080), Image.LANCZOS)
                
                # 저장할 경로 설정
                save_path = os.path.join(output_folder, f'resized_{filename}')
                img.save(save_path)
                print(f'Saved resized image: {save_path}')

# 사용 예시
folder_path = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트와 같은 폴더 경로
resize_and_crop_images(folder_path)
