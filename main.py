from utils import read_video, save_video
def main():
    # Read video
    video_frames = read_video('input_video/08fd33_4.mp4')
    # Save video
    save_video(video_frames, 'output_video/output.avi')

if __name__ == "__main__":
    main()