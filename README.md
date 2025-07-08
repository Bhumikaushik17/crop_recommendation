# 🌾 Crop Recommendation System using Machine Learning

A smart crop recommendation system that helps farmers identify the most suitable crop to grow based on soil and weather conditions using machine learning.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-green?logo=streamlit)](https://your-app-url.streamlit.app)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📌 Overview

This project predicts the **best crop to cultivate** using parameters like:
- 🧪 Nitrogen, Phosphorus, Potassium (NPK)
- 🌡️ Temperature
- 💧 Humidity
- 🧪 pH Level
- 🌧️ Rainfall

The app uses a **Random Forest Classifier** to make accurate predictions and is deployed using **Streamlit** for easy user interaction.

---

## 🔧 Tech Stack

| Tool         | Purpose                         |
|--------------|----------------------------------|
| Python       | Core programming language        |
| Streamlit    | Web app interface                |
| Scikit-learn | Machine Learning library         |
| Pandas/Numpy | Data handling and preprocessing  |
| Pickle       | Model serialization              |

---

## 🚀 Features

✅ Easy-to-use web interface  
✅ Real-time crop recommendation  
✅ Responsive and fast predictions  
✅ Trained on real-world agricultural data  

---


## 📁 Project Structure--

```bash
crop_recommendation/
│
├── app.py               # Streamlit app
├── model.pkl            # Trained machine learning model
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── dataset.csv          # Crop dataset (optional)
-----💡 How to Run Locally
Clone the repository
git clone https://github.com/Bhumikaushik17/crop_recommendation.git
cd crop_recommendation
--
Install dependencies
pip install -r requirements.txt
---
Run the app
streamlit run app.py
---
🧠 Dataset
Source: Kaggle - Crop Recommendation Dataset

Features: N, P, K, temperature, humidity, pH, rainfall

Labels: Crop names (rice, wheat, cotton, etc.)

