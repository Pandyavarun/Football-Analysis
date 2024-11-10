import sys
sys.path.append('../')
from utils import get_center_of_bbox, measure_distance

class PlayerBallAssigner():

    def __init__(self):
        self.max_player_ball_distance = 50

    def assign_player_ball(self, players, ball_bbox):
        ball_position = get_center_of_bbox(ball_bbox)

        mininum_distance = float("inf")
        assigned_player = None

        for player_id, player in players.items():
            player_bbox =  player['bbox']

            distance_left_foot = measure_distance((player_bbox[0], player_bbox[-1]),ball_position )
            distance_right_foot = measure_distance((player_bbox[2], player_bbox[-1]),ball_position )
            distance = min(distance_left_foot, distance_right_foot)

            if distance < mininum_distance:
                mininum_distance = distance
                assigned_player = player_id
        
        return assigned_player