# Model Usage Guide

This guide explains how to load and use the model that was trained using the Campus Landmarks dataset for building classification.

## Requirements

Make sure the following dependencies are installed:
- PyTorch (with torchvision)
- Pillow

You can install them using `pip`:

```bash
pip install torch torchvision pillow
```

## Steps to Run the Model

### 1. Clone the Repository

```bash
git clone https://github.com/MahdiahAqib/Mobile-Based-Campus-Navigation-.git
```

### 2. Load the Trained Model and Weights

The model was saved during training as `model.pth`. To load the model:

```python
import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image

# Define the model structure
model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
num_classes = 6
model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, num_classes)

# Load the trained model weights
model.load_state_dict(torch.load("model.pth", weights_only=True))
```

### 3. Using the loaded model for inference
```python
model.eval()  # Set the model to evaluation mode

# Move model to device (if using GPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def apply_transformations(image_path):
    img = Image.open(image_path).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    img = transform(img)
    return img.unsqueeze(0)  

def predict_building(image):
    processed_image = apply_transformations(image)

    with torch.no_grad():
        output = model(processed_image.to(device))
        predicted_class = torch.argmax(output, dim=1).item()
    
    predicted_label = label_mapping.get(predicted_class, "Unknown")
    print(f"Predicted Building: {predicted_label}")

label_mapping = {
    0: "Block A",
    1: "Block B",
    2: "Block C",
    3: "Block D",
    4: "Block E",
    5: "Block F", 
}

# Test your image
img_path = 'path_to_image.jpg' # Replace with your image path

predict_building(img_path)
```
- Ensure that the model and input image are on the same device (GPU/CPU).
- If you're using a GPU, make sure you have CUDA installed and `torch.cuda.is_available()` is `True`.

### 4. Interpreting the Output
The predicted output will be the block/building the image represents.

# Distance Estimation module (Phase-3)
## Objective
Estimate the distance from the user’s position to a detected landmark by analyzing two images captured from different horizontal positions (left and right views), using visual cues and mathematical models
## Requirements
- Python 3 (Automatically available in Google Colab)
- Torch and Torchvision
- OpenCV
- RoboFlow API (via inference_sdk)
- Google Colab for GUI and file uploads
## Input Format
- Upload exactly 2 images of the same landmark taken from slightly different positions.
- Baseline Distance: 1 meter between the two camera positions (known and fixed).
- Images should be taken at the same height and orientation as much as possible.
## Outputs
The matched object is displayed in both left and right images with:
- Green bounding box
- Red center dot
- Label name

Estimated distance is printed in meters

# 📱 Phase 4 - Mobile App

Access the mobile app repository here: [Campus Navigator Mobile App](https://github.com/RaabiaBaig/Campus-Navigator-Mobile-App)

### How to Run the Mobile App

1. Clone or download the **Campus-Navigator-Mobile-App** repository.
2. Open the project folder and follow these steps:
   
   - Open **two terminals**:
     - **Terminal 1**:
       ```bash
       cd backend
       python app.py
       ```
     - **Terminal 2** (from project root):
       ```bash
       npx expo start
       ```

3. Install the **Expo Go** app on your phone.
4. Scan the QR code shown in the terminal to run the app on your device.
