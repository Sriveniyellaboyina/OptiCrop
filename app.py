from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict_page")
def predict_page():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [float(x) for x in request.form.values()]

    final_features = np.array([features])

    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template(
    "result.html",
    prediction=output
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)