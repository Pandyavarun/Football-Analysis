from utils import read_video, save_video
from trackers import Tracker


def main():
    # Read video
    video_frames = read_video('input_video/08fd33_4.mp4')

    # Create tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracker(video_frames)

    # Save video
    save_video(video_frames, 'output_video/output.avi')

if __name__ == "__main__":
    main()