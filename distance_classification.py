import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import wandb  # For experiment tracking

# Initialize WandB
wandb.init(project="distance_classification_project")

# Generate synthetic dataset
X, y = make_classification(n_samples=500, n_features=5, random_state=42)
df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
df["label"] = y

print(f"✅ Generated synthetic dataset. Shape: {df.shape}")

# Split data into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['label']), df['label'], test_size=0.2, random_state=42)

# Train a k-NN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"🔍 Classification Accuracy: {accuracy:.4f}")

# Log results to WandB
wandb.log({"accuracy": accuracy})