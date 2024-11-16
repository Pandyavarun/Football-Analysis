# Football Analysis

## Overview
This project analyzes football matches using computer vision and machine learning techniques. It integrates multiple technologies, such as YOLO for object detection, K-Means clustering for team identification, and optical flow for tracking player and ball movements. Key capabilities include:

- Detecting and tracking players, referees, and footballs in video footage.
- Assigning players to teams based on t-shirt colors.
- Measuring ball possession percentages for teams.
- Calculating player movements and distances in real-world units using perspective transformation.
- Estimating player speed and distance covered during a match.

---

## Features
- **YOLO-based Object Detection**: Detects players, referees, and the football.
- **Team Identification**: Uses K-Means clustering for color segmentation.
- **Optical Flow**: Tracks object movements and estimates camera motion.
- **Perspective Transformation**: Converts pixel-based measurements into meters.
- **Speed and Distance Metrics**: Evaluates player performance in terms of speed and distance covered.

---

## Getting Started

### Prerequisites
- Python 3.8 or above.
- Required Python libraries (install via `requirements.txt`).

---

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Pandyavarun/Football-Analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Football-Analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Usage

1. **Train YOLOv5 Model**:
   - Open and run the notebook `training/Yolov5.ipynb` to train your YOLOv5 model.
   - After training, copy the generated model (e.g., `best.pt`) to the `models/` folder.

2. **Upload Input Video**:
   - Manually upload your input video into the `input_videos/` folder.
   - Update the video file name in the `main.py` script:
     ```python
     video_frames = read_video('input_videos/your_video_name.mp4')
     ```

3. **Run the Main Script**:
   - Execute the main analysis pipeline:
     ```bash
     python main.py
     ```
   - Processed results, including videos and metrics, will be saved in the `output_videos/` folder.

4. **Inference with YOLO**:
   - Run the YOLO inference script using:
     ```bash
     python yolo_inference.py
     ```

---

## File Structure
- `main.py`: Main script for running the analysis.
- `training/`: Contains the YOLOv5 training notebook (`Yolov5.ipynb`).
- `models/`: Directory for storing pre-trained or newly trained YOLO models.
- `utils/`: Helper scripts for video processing and analysis.
- `input_videos/`: Folder for manually uploaded input videos.
- `output_videos/`: Folder for processed video outputs and metrics.
- `camera_movement_estimator/`: Module for estimating camera movement.
- `player_ball_assigner/`: Assigns balls to players during the match.
- `team_assigner/`: Assigns players to teams based on their jersey color.
- `trackers/`: Includes tracking functionality for players and ball.
- `view_transformer/`: Module for transforming view and position adjustments.
- `speed_and_distance_estimator/`: Estimates player speed and distance.
- `stubs/`: Stores intermediate data like track and camera movement stubs.
- `runs/`: Stores results of detection runs.
- `requirements.txt`: Python dependencies for the project.
- `yolo_inference.py`: Script to run YOLO inference on input videos.

---

## Contributing
We welcome contributions! Fork the repository, create a new branch, and submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or support, open an issue in the repository.
