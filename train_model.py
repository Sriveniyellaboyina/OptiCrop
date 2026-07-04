import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")

# Features and target
X = df.drop("label", axis=1)
y = df["label"]

# Encode target
encoder = LabelEncoder()
y = encoder.fit_transform(y)
joblib.dump(encoder, "model/label_encoder.pkl")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
joblib.dump(scaler, "model/scaler.pkl")

# ---------------- Random Forest ----------------
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_prediction = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_prediction)

print("Random Forest Accuracy:", rf_accuracy)
print(classification_report(y_test, rf_prediction))
print(confusion_matrix(y_test, rf_prediction))

# ---------------- Decision Tree ----------------
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_prediction = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_prediction)

# ---------------- KNN ----------------
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_prediction = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_prediction)

# ---------------- Logistic Regression ----------------
lr_model = LogisticRegression(max_iter=500)
lr_model.fit(X_train, y_train)
lr_prediction = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_prediction)

# Compare Models
print("\nModel Comparison")
print("-" * 30)
print(f"Random Forest       : {rf_accuracy:.4f}")
print(f"Decision Tree       : {dt_accuracy:.4f}")
print(f"KNN                 : {knn_accuracy:.4f}")
print(f"Logistic Regression : {lr_accuracy:.4f}")

# Save best model
joblib.dump(rf_model, "model/crop_model.pkl")

# Test prediction
sample = [[90, 42, 43, 20.879744, 82.002744, 6.502985, 202.935536]]
sample = scaler.transform(sample)

prediction = rf_model.predict(sample)
crop = encoder.inverse_transform(prediction)

print("\nSample Prediction:", crop[0])