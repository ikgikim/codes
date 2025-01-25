import os

def wrap_text_in_files():
    # 현재 작업 디렉토리에서 텍스트 파일 읽기
    folder_path = os.getcwd()  # 현재 경로 가져오기
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # 결과를 저장할 리스트
            wrapped_lines = []

            for line in lines:
                words = line.strip().split()  # 단어 단위로 나누기
                current_line = ""

                for word in words:
                    # 현재 줄에 단어를 추가했을 때 13글자를 넘지 않으면 추가
                    if len(current_line) + len(word) + 1 <= 13:  # +1은 공백을 고려
                        if current_line:
                            current_line += " "  # 공백 추가
                        current_line += word
                    else:
                        # 현재 줄을 결과에 추가하고 새로운 줄 시작
                        wrapped_lines.append(current_line)
                        current_line = word  # 새 줄에 현재 단어 추가

                # 마지막 줄 추가
                if current_line:
                    wrapped_lines.append(current_line)

            # 결과를 새로운 파일에 저장
            output_file_path = os.path.join(folder_path, f'wrapped_{filename}')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for wrapped_line in wrapped_lines:
                    output_file.write(wrapped_line + '\n')

            print(f'파일 "{filename}"에 대한 줄바꿈이 완료되었습니다: {output_file_path}')

# 코드 실행
wrap_text_in_files()
