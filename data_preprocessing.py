import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("dataset/Crop_recommendation.csv")

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

print("\nDuplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

X = df.drop("label", axis=1)
y = df["label"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

joblib.dump(encoder, "model/label_encoder.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, "model/scaler.pkl")

print("\nTraining Feature Shape:", X_train_scaled.shape)
print("Testing Feature Shape:", X_test_scaled.shape)
print("Training Label Shape:", y_train.shape)
print("Testing Label Shape:", y_test.shape)

print("\nData Preprocessing Completed Successfully!")