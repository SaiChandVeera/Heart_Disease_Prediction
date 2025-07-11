# Heart Disease Prediction System 💓

## 📌 Overview

Heart disease is one of the leading causes of death globally. Early detection through predictive modeling can assist healthcare professionals in timely diagnosis and intervention. This system uses machine learning to analyze patient health indicators and predict the likelihood of heart disease.

## 🚀 Features

- Preprocesses and cleans real-world medical data
- Performs Exploratory Data Analysis (EDA)
- Implements K-Nearest Neighbors (KNN) for classification
- Evaluates model performance with accuracy, confusion matrix, and more
- Easy-to-follow code and modular design

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

## 📊 Dataset

The dataset is based on the [UCI Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease), containing the following features:

### Patient Information
- **Age**: Age of the patient
- **Sex**: Gender (male/female)
- **Chest Pain Type**: Different types of chest pain experienced
- **Resting Blood Pressure**: Blood pressure when at rest
- **Cholesterol**: Serum cholesterol level
- **Fasting Blood Sugar**: Blood sugar level after fasting
- **Rest ECG**: Resting electrocardiographic results
- **Maximum Heart Rate**: Maximum heart rate achieved during exercise
- **Exercise Induced Angina**: Chest pain triggered by exercise
- **ST Depression**: Heart rhythm measurement
- **Slope**: Slope of peak exercise ST segment
- **Number of Major Vessels**: Vessels colored by fluoroscopy
- **Thalassemia**: Blood disorder type

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook or Python script:
   ```bash
   jupyter notebook heart_disease_prediction.ipynb
   # OR
   python main.py
   ```

## 📈 Results

- **Model Used**: K-Nearest Neighbors (KNN)
- **Accuracy**: 85% on test dataset
- **Key Findings**: Strong correlations between chest pain type and maximum heart rate with heart disease likelihood
- **Important Predictors**: Chest pain type, maximum heart rate, and exercise-induced angina



## 🔍 Key Insights

- Patients aged 50-65 show higher risk patterns
- Male patients demonstrate higher susceptibility rates
- Exercise-induced angina is a strong predictor of heart disease
- Chest pain type is the most important feature for prediction

## 🚨 Medical Disclaimer

This predictive model is designed for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests for improvements.

---

⭐ **If you found this project helpful, please give it a star!** ⭐
