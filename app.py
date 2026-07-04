from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and preprocessing files
model = joblib.load("model/crop_model.pkl")
scaler = joblib.load("model/scaler.pkl")
encoder = joblib.load("model/label_encoder.pkl")


# ===========================
# Home Page
# ===========================
@app.route("/")
def home():
    return render_template("home.html")


# ===========================
# About Page
# ===========================
@app.route("/about")
def about():
    return render_template("about.html")


# ===========================
# Prediction Page
# ===========================
@app.route("/predict_page")
def predict_page():
    return render_template("predict.html")


# ===========================
# Prediction Route
# ===========================
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from HTML form
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Create DataFrame
        sample = pd.DataFrame([{
            "N": N,
            "P": P,
            "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }])

        # Scale input
        sample_scaled = scaler.transform(sample)

        # Predict
        prediction = model.predict(sample_scaled)

        # Convert numeric prediction to crop name
        crop = encoder.inverse_transform(prediction)

        return render_template(
            "result.html",
            crop=crop[0]
        )

    except Exception as e:

        return render_template(
            "result.html",
            crop="Prediction Failed",
            error=str(e)
        )


# ===========================
# Run Application
# ===========================
if __name__ == "__main__":
    app.run(debug=True)