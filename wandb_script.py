import wandb
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix

# ✅ Initialize Weights & Biases (WandB)
wandb.init(project='distance_classification_project')

# 1️⃣ **Compute a valid metric score (Example: Accuracy)**
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]  # Replace with real labels
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]  # Replace with model predictions

score = accuracy_score(y_true, y_pred)  # Define score properly
print(f"Model Accuracy: {score}")

# 2️⃣ **Load and process an image**
image_path = "/Users/macbook/Downloads/Plaksha_Faculty.jpg"  # Replace with an actual image path
image = cv2.imread(image_path)

# Handle missing image error
if image is None:
    raise ValueError(f"Error: Could not load image at {image_path}")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3️⃣ **Plot the grayscale image**
plt.figure(figsize=(6, 6))
plt.imshow(gray_image, cmap='gray')
plt.title("Processed Grayscale Image")
plt.axis("off")
plt.savefig("grayscale_plot.png")  # Save the figure

# 4️⃣ **Confusion Matrix & Heatmap**
conf_matrix = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues", xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")  # Save the figure

# 5️⃣ **Logging to Weights & Biases**
wandb.log({"Metric Score": score})
wandb.log({"Output Image": wandb.Image(gray_image)})  # Ensure valid image data
wandb.log({"Confusion Matrix": wandb.Image("confusion_matrix.png")})
wandb.log({"Grayscale Image Plot": wandb.Image("grayscale_plot.png")})

print("Successfully logged data, images, and graphs to Weights & Biases.")
