# distance_classification

Author: Arshveer Chhabra

Output Images:
![Project Screenshot](<Screenshot 2025-02-25 at 19.56.13.png>)

![Project Screenshot](<Screenshot 2025-02-25 at 19.56.17.png>)

![Project Screenshot](<Screenshot 2025-02-25 at 19.58.42.png>)

![Project Screenshot](<Screenshot 2025-02-25 at 19.47.35.png>)

![Project Screenshot](<Screenshot 2025-02-25 at 19.47.30.png>)


Report:
### **1. What are the common distance metrics used in distance-based classification algorithms?**  
Distance-based classification algorithms, like **k-Nearest Neighbors (KNN)**, rely on measuring the similarity between data points. The most commonly used distance metrics include:  

- **Euclidean Distance**: The straight-line distance between two points in space. Most widely used in KNN.  
- **Manhattan Distance**: Measures distance along axes at right angles (like city blocks). Works well when data has grid-like structure.  
- **Minkowski Distance**: A generalization of Euclidean and Manhattan distance. The parameter \( p \) controls the metric (when \( p=2 \), it becomes Euclidean; when \( p=1 \), it’s Manhattan).  
- **Cosine Similarity**: Measures the cosine of the angle between two vectors. Common in text and high-dimensional data.  
- **Hamming Distance**: Counts differences in categorical or binary features (e.g., DNA sequences, text).  

Each metric is chosen based on the problem type and dataset characteristics.  

---

### **2. What are some real-world applications of distance-based classification algorithms?**  
Distance-based classification algorithms, especially **KNN**, are widely used across various industries. Some real-world applications include:  

- **Medical Diagnosis**: KNN helps classify diseases by comparing patient symptoms with known cases.  
- **Fraud Detection**: Used in banking and finance to identify suspicious transactions by measuring their "distance" from normal transaction patterns.  
- **Recommendation Systems**: E-commerce platforms like Amazon use distance-based algorithms to suggest products based on user preferences.  
- **Image Recognition**: Facial recognition systems use distance metrics to compare facial features and match them to known identities.  
- **Text Categorization**: Cosine similarity helps in spam detection and sentiment analysis by measuring similarity between text documents.  

These algorithms are especially useful when the decision boundary is non-linear and data is not easily separable.  

---

### **3. Explain various distance metrics.**  

#### **1. Euclidean Distance**

Used when all features have the same scale.  

#### **2. Manhattan Distance**
Works well when movements are restricted to grid-like paths (e.g., chessboard movement).  

#### **3. Minkowski Distance**
A generalized form of Euclidean and Manhattan distance:  

If \( p=1 \), it’s Manhattan; if \( p=2 \), it’s Euclidean.  

#### **4. Cosine Similarity**
Measures the angle between two vectors rather than their absolute difference:  
Common in text classification and NLP.  

#### **5. Hamming Distance**
Counts the number of differing bits in binary data. Used in error detection (e.g., genetic sequences, text matching).  

Each metric has its own advantages depending on the dataset and application.  

---

### **4. What is the role of cross-validation in model performance?**  
Cross-validation helps assess how well a model generalizes to unseen data. Instead of training and testing on a single dataset split, **cross-validation divides the data into multiple parts** and rotates training/testing across them.  

#### **Common Types of Cross-Validation:**  
- **K-Fold Cross-Validation**: The dataset is split into **k** equal parts, and the model is trained on **k-1** folds while the remaining fold is used for testing. This process repeats **k times** to reduce variability.  
- **Leave-One-Out Cross-Validation (LOOCV)**: A special case where only one data point is used for testing, and the rest for training. Computationally expensive but useful for small datasets.  
- **Stratified K-Fold**: Ensures class proportions remain consistent across folds, helpful for imbalanced datasets.  

Cross-validation prevents **overfitting**, ensures robustness, and helps in selecting the best model by providing a more reliable estimate of performance.  

---

### **5. Explain variance and bias in terms of KNN.**  
In **KNN**, the number of neighbors (\( k \)) directly affects the bias-variance tradeoff:  

#### **High Variance (Low \( k \))**
- When **\( k \) is small** (e.g., \( k = 1 \)), the model closely follows the training data.  
- This leads to **overfitting**, as small changes in data drastically alter predictions.  
- The model has **low bias but high variance**, meaning it memorizes patterns instead of generalizing.  

#### **High Bias (Large \( k \))**
- When **\( k \) is large** (e.g., \( k = 20 \)), predictions are based on a broader group of neighbors.  
- This leads to **underfitting**, as the model oversimplifies patterns.  
- The model has **high bias but low variance**, meaning it generalizes too much and ignores local patterns.  

#### **Finding the Right Balance**
- A **moderate \( k \) (e.g., 5-10)** usually achieves a balance between bias and variance.
- Using **cross-validation** helps determine the best \( k \) for a dataset.
