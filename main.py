from utils import read_video, save_video
from trackers import Tracker


def main():
    # Read video
    video_frames = read_video('input_video/08fd33_4.mp4')

    # Create tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracker(video_frames, read_from_stub = True, stub_path = "stubs/track_stub.pkl")

    # Draw Output 

    output_video_frames = tracker.draw_annotations(video_frames, tracks)



    # Save video
    save_video(output_video_frames, 'output_video/output.avi')

if __name__ == "__main__":
    main()