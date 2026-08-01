# 🌱 OptiCrop – Smart Agriculture Production Optimization Engine

OptiCrop is a Machine Learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The application uses a trained **Random Forest** model to help users identify the best crop for cultivation by providing values such as Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.

---

## 🔗 Live Demo


**Deployment URL:** https://opticrop-u9b8.onrender.com

---

## 📌 Features

- Predicts the most suitable crop based on user inputs.
- Modern and responsive web interface built with Flask.
- Fast and accurate predictions using a trained Random Forest model.
- User-friendly interface for crop recommendation.
- Attractive Home, About, Predict Crop, and Result pages.

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- JavaScript
- Pickle

---

## 📂 Project Structure

```text
OptiCrop/
│
├── app.py
├── requirements.txt
├── README.md
├── dataset/
│   └── Crop_recommendation.csv
├── model/
│   └── model.pkl
├── notebooks/
│   └── OptiCrop.ipynb
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── predict.html
│   └── result.html
└── .gitignore
```

---

## 📊 Input Parameters

The prediction model uses the following input features:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH Value
- Rainfall (mm)

---

## 🌾 Output

The application predicts the most suitable crop for cultivation based on the provided input values.

---

## 🤖 Machine Learning

The crop recommendation model was developed using **Random Forest Classifier**. The trained model was saved using Pickle and is loaded by the Flask application to generate real-time crop recommendations.

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/OptiCrop.git
```

### Navigate to the project folder

```bash
cd OptiCrop
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home_page.png)

### About Page

![About Page](screenshots/about_page.png)

### Predict Crop Page

![Predict Crop Page](screenshots/predict_page.png)

### Prediction Result

![Prediction Result](screenshots/result_page.png)

---

## 👨‍💻 Author

**Kushal Sai Kumar Antarvedi**

Project: OptiCrop  
Team ID: SWTID-2026-5714

---

## 📄 License

This project is developed for academic purposes.