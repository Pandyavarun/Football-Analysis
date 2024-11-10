import cv2


def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_path):
    # Set the codec for mp4 format
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Create the VideoWriter object
    out = cv2.VideoWriter(output_path, fourcc, 24.0, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    
    for frame in output_video_frames:
        out.write(frame)
    
    # Release the VideoWriter object
    out.release()
