from utils import read_video, save_video
from trackers import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
import cv2
import numpy as np


def main():
    # Read video
    video_frames = read_video('input_video/08fd33_4.mp4')

    # Create tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracker(video_frames, read_from_stub = True, stub_path = "stubs/track_stub.pkl")

    #Estimate Camera Movement
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames, read_from_stub = True, stub_path = "stubs/camera_movement_stub.pkl")

    #Interpolate Ball Positions

    tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])

    #Assign Team
    team_assigner = TeamAssigner()
    team_ball_control = []
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]


    #Assign Ball Acquisition

    player_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_player_ball(player_track, ball_bbox)
        
        if assigned_player is not None:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])
    team_ball_control = np.array(team_ball_control)

    #Draw Camera Movement
    output_video_frames = CameraMovementEstimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)
    # Draw Output 

    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)



    # Save video
    save_video(output_video_frames, 'output_video/output.avi')

if __name__ == "__main__":
    main()