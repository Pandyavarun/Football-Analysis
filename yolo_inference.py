from ultralytics import YOLO

model = YOLO('models/best.pt')  # Load model

results = model.predict('input_video/08fd33_4.mp4', save=True)  # Inference

print(results[0])
print('"""""""""""""""""""""""""""""""""""""')
for box in results[0].boxes:
    print(box)