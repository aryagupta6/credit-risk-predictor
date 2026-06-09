# Credit Risk Predictor

## Overview

Credit Risk Predictor is a Machine Learning web application that predicts whether a loan applicant is likely to be a **Low Risk** or **High Risk** borrower based on financial and demographic information.

The project uses a **Decision Tree Classifier** trained on a credit risk dataset and is deployed as a web application using **Flask** and **Render**.

---

## Features

* Predicts credit risk in real time
* User-friendly web interface
* Machine Learning based decision making
* Flask backend integration
* Cloud deployment using Render
* Responsive and simple UI

---

## Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Decision Tree Classifier

### Web Development

* Flask
* HTML
* CSS

### Deployment

* GitHub
* Render

---

## Dataset Features

The model uses the following input features:

* Age
* Income
* Loan Amount
* Credit Score
* Employment Years
* Education Level
* Housing Status (Own/Rent)

### Target Variable

* Default

  * 0 → Low Risk
  * 1 → High Risk

---

## Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Encoding
4. Model Training
5. Model Evaluation
6. Model Serialization using Pickle
7. Flask Integration
8. Web Interface Development
9. Deployment on Render

---

## Model Performance

* Algorithm: Decision Tree Classifier
* Accuracy: Approximately 76%

---

## Project Structure

```text
credit-risk-predictor/
│
├── app.py
├── model.pkl
├── credit_risk_dataset.csv
├── requirements.txt
├── project_cse_default.ipynb
│
└── templates/
    └── index.html
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/credit-risk-predictor.git
cd credit-risk-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

* Improved model accuracy using ensemble methods
* Better user interface design
* Advanced feature engineering
* Additional financial indicators
* User authentication and data storage

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* Data preprocessing
* Feature engineering
* Machine Learning model training
* Model evaluation
* Flask web development
* Frontend-backend integration
* Cloud deployment

---

## Author

Arya Gupta

B.Tech Computer Science Engineering

Academic Machine Learning Project
