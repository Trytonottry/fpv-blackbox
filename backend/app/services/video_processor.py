import cv2
import os

def extract_frames(video_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_time = 0
    idx = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if idx % int(fps / 10) == 0:  # 10 кадров в секунду
            cv2.imwrite(f"{output_dir}/frame_{frame_time:.2f}.jpg", frame)
        frame_time += 1 / fps
        idx += 1
    cap.release()