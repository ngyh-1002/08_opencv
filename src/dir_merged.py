import os
import shutil

# 상위 디렉토리 경로
parent_dir = '../img/TS/M1/P10'

# 상위 디렉토리 내의 모든 하위 폴더 순회
for folder in os.listdir(parent_dir):
    folder_path = os.path.join(parent_dir, folder)

    # 폴더인 경우만 처리
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            src_file = os.path.join(folder_path, file)
            dst_file = os.path.join(parent_dir, file)

            # 파일명이 중복될 경우 파일명 뒤에 숫자 추가
            base, ext = os.path.splitext(file)
            count = 1
            while os.path.exists(dst_file):
                dst_file = os.path.join(parent_dir, f"{base}_{count}{ext}")
                count += 1

            shutil.move(src_file, dst_file)

        # 폴더가 비었으므로 삭제
        os.rmdir(folder_path)
